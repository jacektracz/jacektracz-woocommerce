this.wc=this.wc||{},this.wc.blocks=this.wc.blocks||{},this.wc.blocks["product-search"]=function(e){function t(t){for(var n,a,l=t[0],i=t[1],s=t[2],b=0,d=[];b<l.length;b++)a=l[b],Object.prototype.hasOwnProperty.call(r,a)&&r[a]&&d.push(r[a][0]),r[a]=0;for(n in i)Object.prototype.hasOwnProperty.call(i,n)&&(e[n]=i[n]);for(u&&u(t);d.length;)d.shift()();return o.push.apply(o,s||[]),c()}function c(){for(var e,t=0;t<o.length;t++){for(var c=o[t],n=!0,l=1;l<c.length;l++){var i=c[l];0!==r[i]&&(n=!1)}n&&(o.splice(t--,1),e=a(a.s=c[0]))}return e}var n={},r={14:0},o=[];function a(t){if(n[t])return n[t].exports;var c=n[t]={i:t,l:!1,exports:{}};return e[t].call(c.exports,c,c.exports,a),c.l=!0,c.exports}a.m=e,a.c=n,a.d=function(e,t,c){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:c})},a.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var c=Object.create(null);if(a.r(c),Object.defineProperty(c,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)a.d(c,n,function(t){return e[t]}.bind(null,n));return c},a.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="";var l=window.webpackWcBlocksJsonp=window.webpackWcBlocksJsonp||[],i=l.push.bind(l);l.push=t,l=l.slice();for(var s=0;s<l.length;s++)t(l[s]);var u=i;return o.push([596,2,1,0]),c()}({0:function(e,t){!function(){e.exports=this.wp.element}()},1:function(e,t){!function(){e.exports=this.wp.i18n}()},12:function(e,t,c){"use strict";c.d(t,"d",(function(){return r})),c.d(t,"n",(function(){return o})),c.d(t,"i",(function(){return a})),c.d(t,"k",(function(){return l})),c.d(t,"a",(function(){return i})),c.d(t,"j",(function(){return s})),c.d(t,"m",(function(){return u})),c.d(t,"c",(function(){return b})),c.d(t,"l",(function(){return d})),c.d(t,"b",(function(){return p})),c.d(t,"g",(function(){return g})),c.d(t,"h",(function(){return h})),c.d(t,"e",(function(){return f})),c.d(t,"f",(function(){return m})),c.d(t,"o",(function(){return w}));var n=c(5),r=Object(n.getSetting)("enableReviewRating",!0),o=Object(n.getSetting)("showAvatars",!0),a=Object(n.getSetting)("max_columns",6),l=Object(n.getSetting)("min_columns",1),i=Object(n.getSetting)("default_columns",3),s=Object(n.getSetting)("max_rows",6),u=Object(n.getSetting)("min_rows",1),b=Object(n.getSetting)("default_rows",2),d=Object(n.getSetting)("min_height",500),p=Object(n.getSetting)("default_height",500),g=(Object(n.getSetting)("placeholderImgSrc",""),Object(n.getSetting)("thumbnail_size",300),Object(n.getSetting)("isLargeCatalog")),h=Object(n.getSetting)("limitTags"),f=(Object(n.getSetting)("hasProducts",!0),Object(n.getSetting)("hasTags",!0)),m=Object(n.getSetting)("homeUrl",""),w=(Object(n.getSetting)("productCount",0),Object(n.getSetting)("attributes",[]),Object(n.getSetting)("wcBlocksAssetUrl",""))},194:function(e,t,c){var n=c(579);"string"==typeof n&&(n=[[e.i,n,""]]);var r={insert:"head",singleton:!1};c(35)(n,r);n.locals&&(e.exports=n.locals)},21:function(e,t){!function(){e.exports=this.wp.editor}()},22:function(e,t){!function(){e.exports=this.wp.compose}()},25:function(e,t){!function(){e.exports=this.wp.blocks}()},3:function(e,t){!function(){e.exports=this.wp.components}()},5:function(e,t){!function(){e.exports=this.wc.wcSettings}()},579:function(e,t,c){},596:function(e,t,c){"use strict";c.r(t);var n=c(0),r=c(1),o=c(25),a=c(3),l=(c(193),c(194),c(6)),i=c.n(l),s=(c(2),c(12)),u=function(e){var t=e.attributes,c=t.label,o=t.placeholder,a=t.formId,l=t.className,u=t.hasLabel,b=t.align,d=i()("wc-block-product-search",b?"align"+b:"",l);return Object(n.createElement)("div",{className:d},Object(n.createElement)("form",{role:"search",method:"get",action:s.f},Object(n.createElement)("label",{htmlFor:a,className:u?"wc-block-product-search__label":"wc-block-product-search__label screen-reader-text"},c),Object(n.createElement)("div",{className:"wc-block-product-search__fields"},Object(n.createElement)("input",{type:"search",id:a,className:"wc-block-product-search__field",placeholder:o,name:"s"}),Object(n.createElement)("input",{type:"hidden",name:"post_type",value:"product"}),Object(n.createElement)("button",{type:"submit",className:"wc-block-product-search__button",label:Object(r.__)("Search",'woocommerce')},Object(n.createElement)("svg",{"aria-hidden":"true",role:"img",focusable:"false",className:"dashicon dashicons-arrow-right-alt2",xmlns:"http://www.w3.org/2000/svg",width:"20",height:"20",viewBox:"0 0 20 20"},Object(n.createElement)("path",{d:"M6 15l5-5-5-5 1-2 7 7-7 7z"}))))))},b=c(21),d=c(22),p=Object(d.withInstanceId)((function(e){var t=e.attributes,c=t.label,o=t.placeholder,l=t.formId,s=t.className,u=t.hasLabel,d=t.align,p=e.instanceId,g=e.setAttributes,h=i()("wc-block-product-search",d?"align"+d:"",s);return l||g({formId:"wc-block-product-search-".concat(p)}),Object(n.createElement)(n.Fragment,null,Object(n.createElement)(b.InspectorControls,{key:"inspector"},Object(n.createElement)(a.PanelBody,{title:Object(r.__)("Content",'woocommerce'),initialOpen:!0},Object(n.createElement)(a.ToggleControl,{label:Object(r.__)("Show search field label",'woocommerce'),help:u?Object(r.__)("Label is visible.",'woocommerce'):Object(r.__)("Label is hidden.",'woocommerce'),checked:u,onChange:function(){return g({hasLabel:!u})}}))),Object(n.createElement)("div",{className:h},!!u&&Object(n.createElement)(b.PlainText,{className:"wc-block-product-search__label",value:c,onChange:function(e){return g({label:e})}}),Object(n.createElement)("div",{className:"wc-block-product-search__fields"},Object(n.createElement)(b.PlainText,{className:"wc-block-product-search__field input-control",value:o,onChange:function(e){return g({placeholder:e})}}),Object(n.createElement)("button",{type:"submit",className:"wc-block-product-search__button",label:Object(r.__)("Search",'woocommerce'),onClick:function(e){return e.preventDefault()},tabIndex:"-1"},Object(n.createElement)("svg",{"aria-hidden":"true",role:"img",focusable:"false",className:"dashicon dashicons-arrow-right-alt2",xmlns:"http://www.w3.org/2000/svg",width:"20",height:"20",viewBox:"0 0 20 20"},Object(n.createElement)("path",{d:"M6 15l5-5-5-5 1-2 7 7-7 7z"}))))))}));Object(o.registerBlockType)("woocommerce/product-search",{title:Object(r.__)("Product Search",'woocommerce'),icon:{src:Object(n.createElement)((function(e){var t=e.className;return Object(n.createElement)(a.Icon,{className:t,icon:Object(n.createElement)("svg",{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 25 23"},Object(n.createElement)("path",{d:"M13.0993 2.41207V2.01231C13.0993 0.912976 12.1999 0.0135193 11.1005 0.0135193H4.80435C3.70501 0.0135193 2.80556 0.912976 2.80556 2.01231V5.41026H21.1944V4.5108C21.1944 3.41147 20.295 2.51201 19.1957 2.51201H13.0993V2.41207Z"}),Object(n.createElement)("path",{d:"M8.60759 11.3092C7.50759 12.4092 7.50759 14.2092 8.60759 15.3092C9.70759 16.4092 11.5076 16.4092 12.6076 15.3092C13.7076 14.2092 13.7076 12.4092 12.6076 11.3092C11.5076 10.2092 9.70759 10.2092 8.60759 11.3092Z"}),Object(n.createElement)("path",{d:"M22.0076 7.10919H2.00759C0.80759 7.10919 -0.0924101 8.10919 0.00758988 9.30919L0.70759 20.4092C0.80759 21.5092 1.70759 22.3092 2.70759 22.3092H21.2076C22.3076 22.3092 23.2076 21.5092 23.2076 20.4092L24.0076 9.30919C24.1076 8.10919 23.1076 7.10919 22.0076 7.10919ZM16.5076 20.2092L13.4076 17.1092V16.5092L13.3076 16.4092C11.7076 17.8092 9.30759 17.7092 7.80759 16.2092C6.20759 14.6092 6.20759 12.0092 7.80759 10.4092C9.40759 8.80919 12.0076 8.80919 13.6076 10.4092C15.1076 11.9092 15.2076 14.3092 13.8076 15.9092L13.9076 16.0092H14.4076L17.5076 19.1092L16.5076 20.2092Z"}))})}),null),foreground:"#96588a"},category:"woocommerce",keywords:[Object(r.__)("WooCommerce",'woocommerce')],description:Object(r.__)("Help visitors find your products.",'woocommerce'),supports:{align:["wide","full"]},example:{attributes:{hasLabel:!0}},attributes:{hasLabel:{type:"boolean",default:!0},label:{type:"string",default:Object(r.__)("Search",'woocommerce'),source:"text",selector:"label"},placeholder:{type:"string",default:Object(r.__)("Search products...",'woocommerce'),source:"attribute",selector:"input.wc-block-product-search__field",attribute:"placeholder"},formId:{type:"string",default:""}},edit:p,save:function(e){return Object(n.createElement)("div",null,Object(n.createElement)(u,e))}})}});
