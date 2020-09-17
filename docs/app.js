!function() {
  window.app = {
    $http: http(),
    info: { tzHours: -(new Date().getTimezoneOffset()/60) },
    keys: { segment: 'WmlbvdtG9hJU7p75UIGtZcZbnpg8ibkC' },
    data: { account: { }, user: { } },
  };

  document.readyState === 'complete' ? start() :
    document.addEventListener('readystatechange', function() { document.readyState === 'complete' && start(); });

  function start() {
    var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(!analytics.invoked){analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t,e){var n=document.createElement("script");n.type="text/javascript";n.async=!0;n.src="https://cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(n,a);analytics._loadOptions=e};analytics.SNIPPET_VERSION="4.1.0";
      analytics.load(app.keys.segment);
    }

    app.$http.post('app', 'www').then(function(data) {
      app.data.account = data.account;
      app.data.user = data.user;

      identify();
    });
  }

  function identify() {
    console.log('identify', app.data.user.id)
    if(!app.data.user.id) {
      return;
    }

    window.analytics.identify(app.data.user.id, { }, {
      Intercom: { user_hash: app.data.user.id_hash_intercom }
    });
    window.analytics.page();
  }

  function http() {
    return {
      request: function(method, subdomain, path, options) {
        const url = 'https://'+subdomain+'.trychameleon.com/'+path.replace(/^\//, '');
        const ajax = {
          method: method,
          credentials: 'include',
          mode: 'cors',
          body: JSON.stringify(options),
          headers: {
            'X-Account-Id': window.app.data.account.id,
            'X-Tz-Offset': window.app.info.tzHours,
            'Content-Type': 'application/json',
          }
        };

        return window.fetch(url, ajax).then(function(response) {
          return response.json();
        });
      },
      post: function(subdomain, path, options) {
        return app.$http.request('POST', subdomain, path , options);
      }
    }
  }
}();
