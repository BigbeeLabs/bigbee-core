// assets/js/bigbee_core/html_body.js
(() => {
  const bound = new WeakSet();

  function coerce(detail) {
    if (detail == null) return null;
    if (typeof detail === "string") return detail;
    if (detail instanceof Node) return detail;
    if (typeof detail === "object") return detail.html || detail.body || detail.content || null;
    return null;
  }

  function replace(el, payload) {
    if (payload instanceof Node) el.replaceChildren(payload);
    else if (typeof payload === "string") el.innerHTML = payload;
    else console.warn("replace:html-body missing payload", payload);
  }

  window.BigbeeCore_HtmlBody = {
    initialize(el) {
      if (bound.has(el)) return;
      bound.add(el);

      el.addEventListener("replace:html-body", (evt) => {
        replace(el, coerce(evt.detail));
        window.ComponentInitializer.initialize(el);
      });

      el.addEventListener("remote:error", (evt) => {
        console.warn("⚠️ HtmlBody remote:error", evt.detail);
      });
    }
  };

  // Try to register if the runner is already loaded
  window.registerInitializer?.("BigbeeCore_HtmlBody", window.BigbeeCore_HtmlBody);

  // Ensure initializers run even if this file loads AFTER DOMContentLoaded
  const boot = () => window.runInitializers?.(document);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot, { once: true });
  } else {
    setTimeout(boot, 0);
  }
})();
