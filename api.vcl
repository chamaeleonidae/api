sub vcl_recv {
#FASTLY recv

  # Chameleon:BN - Forward requests to the observe backend
  #
  if (req.url ~ "^/v\d/observe/") {
    set req.backend = F_observe_trychameleon_com;
    set req.url = regsub(req.url, "/observe/", "/");
  }
  # Chameleon:BN - Forward requests to the edit backend
  #
  elsif (req.url ~ "^/v\d/edit/") {
    set req.backend = F_edit_trychameleon_com;
    set req.url = regsub(req.url, "/edit/", "/");
  }
  # Chameleon:BN - Forward requests to the integral backend
  #
  elsif (req.url ~ "^/v\d/integral/") {
    set req.backend = F_integral_trychameleon_com;
    set req.url = regsub(req.url, "/integral/", "/");
  }
  # Chameleon:BN - Forward requests to the forage-analyze backend
  #
  elsif (req.url ~ "^/v\d/analyze/") {
    set req.backend = F_analyze_trychameleon_com;
    set req.url = regsub(req.url, "/analyze/", "/");
  }
  # Chameleon:BN - Proxy all other requests to app.trychameleon.com with the full url intact
  #
  else {
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

  if (beresp.status == 500 || beresp.status == 503) {
    set req.http.Fastly-Cachetype = "ERROR";
    set beresp.ttl = 1s;
    set beresp.grace = 5s;
    return(deliver);
  }

  # Chameleon:BN Do a similar thing to 500/503 when a static asset is a 404 (i.e. it should not be missing so don't cache is as missing)
  #
  if (beresp.status == 404 && req.http.X-Dashboard-Static-Asset) {
    set req.http.Fastly-Cachetype = "ERROR";
    set beresp.ttl = 10s;
    set beresp.grace = 20s;
    return(deliver);
  }

  if (beresp.http.Expires || beresp.http.Surrogate-Control ~ "max-age" || beresp.http.Cache-Control ~ "(s-maxage|max-age)") {
    # keep the ttl here
  } else {
    # apply the default ttl
    set beresp.ttl = 3600s;
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
  set resp.http.Via = "1.1 trychameleon.com (Api)";

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
