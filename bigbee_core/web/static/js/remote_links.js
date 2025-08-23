(() => {
  const fire = (el, name, detail) =>
    el.dispatchEvent(new CustomEvent(name, { bubbles: true, detail }));

  const parseBody = async (res) => {
    const ct = (res.headers.get("content-type") || "").toLowerCase();
    if (ct.includes("application/json")) {
      return { json: await res.json(), contentType: ct };
    }
    return { html: await res.text(), contentType: ct };
  };

  // Remote links (GET only)
  document.addEventListener("click", async (e) => {
    const a = e.target.closest('a[data-remote="true"]');
    if (!a) return;

    // allow new tab / modified clicks
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    e.preventDefault();

    const href = a.getAttribute("href") || location.href;

    try {
      const res = await fetch(href, {
        method: "GET",
        credentials: "same-origin",
        headers: { "X-Remote": "1" },
      });

      const { contentType, ...body } = await parseBody(res);

      if (!res.ok) {
        fire(a, "remote:error", { ...body, url: res.url || href, status: res.status, contentType });
        return;
      }

      fire(a, "remote:success", { ...body, url: res.url || href, status: res.status, contentType });
    } catch (error) {
      fire(a, "remote:error", { error });
      console.error(error);
    }
  });
})();