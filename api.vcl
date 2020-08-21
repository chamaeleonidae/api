sub vcl_recv {
#FASTLY recv

  # Chameleon:BN add default request headers when forwarding to backend
  set req.http.X-Fastly-Api = server.hostname;

  # Chameleon:BN - Forward requests to the observe backend
  #
  if (req.url ~ "^/v3/observe") {
    set req.http.X-Fastly-Backend = "observe";
    set req.backend = F_observe_trychameleon_com;
    set req.url = regsub(req.url, "^/v3/observe", "/v3");
  }
  # Chameleon:BN - Forward requests to the edit backend
  #
  elsif (req.url ~ "^/v3/edit") {
    set req.http.X-Fastly-Backend = "edit";
    set req.backend = F_edit_trychameleon_com;
    set req.url = regsub(req.url, "^/v3/edit", "/v3");
  }
  # Chameleon:BN - Forward requests to the integral backend
  #
  elsif (req.url ~ "^/v3/integral") {
    set req.http.X-Fastly-Backend = "integral";
    set req.backend = F_integral_trychameleon_com;
    set req.url = regsub(req.url, "^/v3/integral", "/v3");
  }
  # Chameleon:BN - Forward requests to the forage-analyze backend
  #
  elsif (req.url ~ "^/v3/analyze") {
    set req.http.X-Fastly-Backend = "analyze";
    set req.backend = F_analyze_trychameleon_com;
    set req.url = regsub(req.url, "^/v3/analyze", "/v3");
  }
  # Chameleon:BN - Proxy all other requests to app.trychameleon.com with the full url intact
  #
  else {
    set req.http.X-Fastly-Backend = "app";
    set req.backend = F_app_trychameleon_com;
  }

  # Chameleon:BN - Security layer for PURGE requests via => https://docs.fastly.com/en/guides/authenticating-api-purge-requests
  #
  if (req.method == "FASTLYPURGE") {
    set req.http.Fastly-Purge-Requires-Auth = "1";
  }

  if (req.method != "HEAD" && req.method != "GET" && req.method != "FASTLYPURGE") {
    return(pass);
  }

  return(lookup);
}

sub vcl_fetch {
  #FASTLY fetch

  if (beresp.http.Set-Cookie) {
    set req.http.Fastly-Cachetype = "SETCOOKIE";
    return(pass);
  }

  if (beresp.http.Cache-Control ~ "private") {
    set req.http.Fastly-Cachetype = "PRIVATE";
    return(pass);
  }

  if (beresp.status == 403 || beresp.status == 404 || beresp.status == 500 || beresp.status == 503) {
    set req.http.Fastly-Cachetype = "ERROR";
    return(pass);
  }

  if (beresp.http.Expires || beresp.http.Surrogate-Control ~ "max-age" || beresp.http.Cache-Control ~ "(s-maxage|max-age)") {
    # keep the ttl here
  } else {
    # apply the default ttl
    set beresp.ttl = 0s;
  }

  return(deliver);
}

sub vcl_hit {
  #FASTLY hit

  if (!obj.cacheable) {
    return(pass);
  }
  return(deliver);
}

sub vcl_miss {
  #FASTLY miss
  return(fetch);
}

sub vcl_deliver {
  #FASTLY deliver

  # Chameleon:BN We should identify ourselves since we're awesome
  #
  set resp.http.Via = "1.1 trychameleon.com (API - " + req.http.X-Fastly-Backend + ")";

  unset resp.http.Server;
  unset resp.http.Age;
  unset resp.http.X-Served-By;
  unset resp.http.X-Cache;
  unset resp.http.X-Cache-Hits;
  unset resp.http.X-Cache-Debug;
  unset resp.http.X-Backend-Key;
  unset resp.http.X-Timer;

  # Chameleon:BN Remove Heroku headers
  #
  unset resp.http.X-Request-Id;
  unset resp.http.X-Runtime;
  unset resp.http.X-Frame-Options;
  unset resp.http.X-Xss-Protection;
  unset resp.http.X-Content-Type-Options;
  unset resp.http.X-Download-Options;
  unset resp.http.X-Permitted-Cross-Domain-Policies;
  unset resp.http.Referrer-Policy;
  unset resp.http.Accept-Ranges;

  return(deliver);
}

sub vcl_error {
  #FASTLY error
}

sub vcl_pass {
  #FASTLY pass
}

sub vcl_log {
  #FASTLY log
}

sub vcl_hash {

  set req.hash += req.url;
  set req.hash += req.http.host;

  #FASTLY hash

  return(hash);
}
