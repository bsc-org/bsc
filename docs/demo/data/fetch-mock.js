(function () {
  const demoBase = './data';
  const realFetch = window.fetch.bind(window);
  let valuesCache = null;

  const fileMap = {
    '/restapi': 'restapi.json',
    '/restapi/errors/active': 'errors_active.json',
    '/restapi/io': 'io.json',
    '/log': 'log.txt',
    '/trigger': 'trigger.txt'
  };

  async function respondJson(data) {
    return new Response(JSON.stringify(data), {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  async function loadValues() {
    if (valuesCache !== null) return valuesCache;
    try {
      const resp = await realFetch(`${demoBase}/values.json`);
      valuesCache = await resp.json();
    } catch (err) {
      valuesCache = {};
    }
    return valuesCache;
  }

  function coerceValue(raw) {
    if (raw === null || raw === undefined) return '';
    const str = String(raw);
    if (/^-?\d+$/.test(str)) return Number(str);
    return str;
  }

  async function applySetValues(urlObj, init) {
    const values = await loadValues();
    const params = new URLSearchParams(urlObj.search);

    if (init && init.body) {
      if (init.body instanceof URLSearchParams) {
        for (const [key, val] of init.body.entries()) params.append(key, val);
      } else if (typeof init.body === 'string') {
        const bodyParams = new URLSearchParams(init.body);
        for (const [key, val] of bodyParams.entries()) params.append(key, val);
      } else if (init.body instanceof FormData) {
        for (const [key, val] of init.body.entries()) params.append(key, val);
      }
    }

    for (const [key, val] of params.entries()) {
      if (!/^\d+$/.test(key)) continue;
      values[key] = coerceValue(val);
    }
  }

  window.fetch = async function (input, init) {
    const url = typeof input === 'string' ? input : input.url;
    const urlObj = new URL(url, window.location.href);
    const path = urlObj.pathname + urlObj.search;

    if (fileMap[path]) {
      return realFetch(`${demoBase}/${fileMap[path]}`, init);
    }

    if (path.startsWith('/p_')) {
      return realFetch(`${demoBase}/${path.slice(1)}.json`, init);
    }

    if (path.startsWith('/getValues?')) {
      const values = await loadValues();
      const query = path.split('?', 2)[1] || '';
      const params = new URLSearchParams(query);
      const data = [];
      for (const key of params.keys()) {
        data.push({ id: Number(key), val: key in values ? values[key] : 0 });
      }
      return respondJson(data);
    }

    if (urlObj.pathname === '/setValues') {
      await applySetValues(urlObj, init);
      return respondJson([]);
    }

    if (path.startsWith('/appreaddata') || path.startsWith('/appwritedata')) {
      return respondJson([]);
    }

    if (path.startsWith('/apptimer')) {
      return new Response('', { headers: { 'Content-Type': 'text/plain' } });
    }

    return realFetch(input, init);
  };
})();
