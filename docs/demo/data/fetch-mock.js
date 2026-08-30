(function () {
  const demoBase = './data';
  const realFetch = window.fetch.bind(window);
  let valuesCache = null;
  const namedDataCache = {};

  const fileMap = {
    '/restapi': 'restapi.json',
    '/restapi/errors/active': 'errors_active.json',
    '/restapi/io': 'io.json',
    '/log': 'log.txt',
    '/trigger': 'trigger.txt',
    '/setup_assistant': 'setup_assistant.json'
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

  async function loadNamedData(fileName) {
    if (Object.prototype.hasOwnProperty.call(namedDataCache, fileName)) {
      return namedDataCache[fileName];
    }
    try {
      const resp = await realFetch(`${demoBase}/${fileName}`);
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();
      namedDataCache[fileName] = data && typeof data === 'object' ? data : {};
    } catch (err) {
      namedDataCache[fileName] = {};
    }
    return namedDataCache[fileName];
  }

  async function respondNamedData(urlObj, fileName) {
    const allData = await loadNamedData(fileName);
    const names = (urlObj.searchParams.get('names') || '')
      .split(',')
      .map(name => name.trim())
      .filter(Boolean);
    const selected = {};
    for (const name of names) {
      if (Object.prototype.hasOwnProperty.call(allData, name)) selected[name] = allData[name];
    }
    return respondJson(selected);
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

    if (urlObj.pathname === '/combos') {
      return respondNamedData(urlObj, 'combos.json');
    }

    if (urlObj.pathname === '/refs') {
      return respondNamedData(urlObj, 'refs.json');
    }

    if (urlObj.pathname.startsWith('/refs/')) {
      const refs = await loadNamedData('refs.json');
      const name = decodeURIComponent(urlObj.pathname.slice('/refs/'.length));
      return respondJson(Object.prototype.hasOwnProperty.call(refs, name) ? refs[name] : {});
    }

    if (urlObj.pathname === '/restapi/vars') {
      const demoVars = {
        board_type: 'default',
        bte_available: 1,
        se_available: 1,
        rico_available: 1
      };
      const result = {};
      const keys = (urlObj.searchParams.get('keys') || '').split(',').map(key => key.trim()).filter(Boolean);
      for (const key of keys) {
        if (Object.prototype.hasOwnProperty.call(demoVars, key)) result[key] = demoVars[key];
      }
      return respondJson(result);
    }

    if (path.startsWith('/p_')) {
      const response = await realFetch(`${demoBase}/${path.slice(1)}.json`, init);
      if (response.ok) return response;
      // Optional settings pages are not present in every demo data set. An
      // empty page keeps the settings export usable instead of aborting its
      // complete request chain on the first missing file.
      return respondJson({ page: [], btn: [], timer: [] });
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
      return respondJson({ state: 1 });
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
