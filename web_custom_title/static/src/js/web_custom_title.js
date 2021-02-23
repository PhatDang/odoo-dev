odoo.define("web_custom_title.Custom_WebTitle", function (require) {
  "use strict";

  // ==================================================================
  // INHERIT: Override CORE Odoo to be custom Web Title on Web Browser.
  // ==================================================================

  var WebClient = require("web.WebClient")

  WebClient.include({
    init: function () {
      this._super.apply(this, arguments);
      this.set("title_part", { zopenerp: document.title });
    },
  });
});
