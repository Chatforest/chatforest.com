(function () {
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var meta = document.getElementById('search-meta');
  var index = null;

  fetch('/index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      index = data;
      // Check for ?q= parameter
      var params = new URLSearchParams(window.location.search);
      var q = params.get('q');
      if (q) {
        input.value = q;
        doSearch(q);
      }
    });

  input.addEventListener('input', function () {
    doSearch(this.value);
  });

  function doSearch(query) {
    if (!index) return;
    var q = query.toLowerCase().trim();
    if (q.length < 2) {
      results.innerHTML = '';
      meta.textContent = '';
      return;
    }

    var terms = q.split(/\s+/);
    var matches = index.filter(function (item) {
      var text = (item.title + ' ' + item.description).toLowerCase();
      return terms.every(function (t) { return text.indexOf(t) !== -1; });
    });

    meta.textContent = matches.length + ' result' + (matches.length !== 1 ? 's' : '');

    if (matches.length === 0) {
      results.innerHTML = '<p class="search-empty">No results found. Try different keywords.</p>';
      return;
    }

    var html = '';
    for (var i = 0; i < matches.length; i++) {
      var m = matches[i];
      html += '<div class="article-card">' +
        '<div class="card-meta"><span>' + capitalize(m.section) + '</span></div>' +
        '<h3><a href="' + m.url + '">' + escapeHtml(m.title) + '</a></h3>' +
        '<p>' + escapeHtml(m.description) + '</p>' +
        '</div>';
    }
    results.innerHTML = html;
  }

  function capitalize(s) {
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  function escapeHtml(s) {
    var d = document.createElement('div');
    d.textContent = s;
    return d.innerHTML;
  }
})();
