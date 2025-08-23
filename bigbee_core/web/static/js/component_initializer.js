// assets/js/component_initializer.js
(() => {
  const InitializerRegistry = new Map();

  function registerInitializer(name, fnOrObj) {
    InitializerRegistry.set(name, fnOrObj);
  }

  function resolveInitializer(name) {
    if (InitializerRegistry.has(name)) return InitializerRegistry.get(name);
    return name.split(".").reduce((o, p) => (o ? o[p] : undefined), window);
  }

  function invokeInitializer(name, el) {
    const ref = resolveInitializer(name);
    if (typeof ref === "function") {
      ref(el);
      return;
    }
    if (ref && typeof ref.initialize === "function") {
      ref.initialize(el);
      return;
    }
    console.warn(`Initializer '${name}' not found or missing .initialize()`);
  }

  function initialize(root = document) {
    root.querySelectorAll("[data-initializers]").forEach((el) => {
      const names = (el.dataset.initializers || "")
        .split(/\s+/)
        .filter(Boolean);

      names.forEach((name) => invokeInitializer(name, el));

      // strip the attribute so it doesn’t run twice
      el.removeAttribute("data-initializers");
    });
  }

  // ✅ Rails-style global name, as you want
  window.ComponentInitializer = {
    initialize,
    register: registerInitializer,
  };

  // auto-run once on DOM ready
  document.addEventListener("DOMContentLoaded", () => initialize());
})();