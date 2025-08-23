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

  // Remote forms
  document.addEventListener("submit", async (e) => {
    const form = e.target;
    if (!form.matches('form[data-remote="true"]')) return;

    e.preventDefault();

    const action = form.getAttribute("action") || location.href;
    const method = (form.getAttribute("method") || "post").toUpperCase();

    try {
      const res = await fetch(action, {
        method,
        body: new FormData(form), // includes hidden csrftoken
        credentials: "same-origin",
        headers: { "X-Remote": "1" },
      });

      const { contentType, ...body } = await parseBody(res);

      if (!res.ok) {
        fire(form, "remote:error", { ...body, url: res.url || action, status: res.status, contentType });
        return;
      }

      console.log("remote:success");
      fire(form, "remote:success", { ...body, url: res.url || action, status: res.status, contentType });
    } catch (error) {
      fire(form, "remote:error", { error });
      console.error(error);
    }
  });
})();