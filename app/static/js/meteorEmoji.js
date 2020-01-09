! function (f) {
    if ("object" == typeof exports && "undefined" != typeof module) module.exports = f();
    else if ("function" == typeof define && define.amd) define([], f);
    else {
        ("undefined" != typeof window ? window : "undefined" != typeof global ? global : "undefined" != typeof self ? self : this).MeteorEmoji = f()
    }
}(function () {
    return function e(t, n, r) {
        function s(o, u) {
            if (!n[o]) {
                if (!t[o]) {
                    var a = "function" == typeof require && require;
                    if (!u && a) return a(o, !0);
                    if (i) return i(o, !0);
                    var f = new Error("Cannot find module '" + o + "'");
                    throw f.code = "MODULE_NOT_FOUND", f
                }
                var l = n[o] = {
                    exports: {}
                };
                t[o][0].call(l.exports, function (e) {
                    var n = t[o][1][e];
                    return s(n || e)
                }, l, l.exports, e, t, n, r)
            }
            return n[o].exports
        }
        for (var i = "function" == typeof require && require, o = 0; o < r.length; o++) s(r[o]);
        return s
    }({
        1: [function (require, module, exports) {
            ! function (global, factory) {
                if (void 0 !== exports) factory(module);
                else {
                    var mod = {
                        exports: {}
                    };
                    factory(mod), global.meteorEmoji = mod.exports
                }
            }(this, function (module) {
                "use strict";
                var _createClass = function () {
                        function defineProperties(target, props) {
                            for (var i = 0; i < props.length; i++) {
                                var descriptor = props[i];
                                descriptor.enumerable = descriptor.enumerable || !1, descriptor.configurable = !0, "value" in descriptor && (descriptor.writable = !0), Object.defineProperty(target, descriptor.key, descriptor)
                            }
                        }
                        return function (Constructor, protoProps, staticProps) {
                            return protoProps && defineProperties(Constructor.prototype, protoProps), staticProps && defineProperties(Constructor, staticProps), Constructor
                        }
                    }(),
                    MeteorEmoji = function () {
                        function MeteorEmoji() {
                            ! function (instance, Constructor) {
                                if (!(instance instanceof Constructor)) throw new TypeError("Cannot call a class as a function")
                            }(this, MeteorEmoji), this.initiate()
                        }
                        return _createClass(MeteorEmoji, [{
                            key: "initiate",
                            value: function () {
                                var _this = this;
                                document.querySelectorAll('[data-meteor-emoji="true"], [data-meteor-emoji-large="true"]').forEach(function (element) {
                                    _this.generateElements(element)
                                })
                            }
                        }, {
                            key: "generateElements",
                            value: function (emojiInput) {
                                var clickLink = function (event) {
                                        var caretPos = emojiInput.selectionStart;
                                        emojiInput.value = (emojiInput.value.substring(0, caretPos) + event.target.innerHTML + emojiInput.value.substring(caretPos) + " ").trim(), emojiPicker.style.display = "block", "undefined" != typeof angular && angular.element(emojiInput).triggerHandler("change");
                                        emojiInput.select();
                                        emojiInput.selectionStart = caretPos + 2;
                                    },
                                    clickCategory = function (event) {
                                        emojiPicker.style.display = "block";
                                        for (var hideUls = emojiPicker.querySelectorAll("ul"), i = 1, l = hideUls.length; i < l; i++) hideUls[i].style.display = "none";
                                        var backgroundToggle = emojiPicker.querySelectorAll(".category a");
                                        for (i = 0, l = backgroundToggle.length; i < l; i++) backgroundToggle[i].style.background = "none";
                                        emojiPicker.querySelector("." + event.target.id).style.display = "flex", emojiPicker.querySelector("#" + event.target.id).style.background = "#c2c2c2"
                                    };
                                emojiInput.style.width = "100%";
                                var emojiContainer = document.createElement("div");
                                emojiContainer.style.position = "relative", emojiInput.parentNode.replaceChild(emojiContainer, emojiInput), emojiContainer.appendChild(emojiInput);
                                var emojiPicker = document.createElement("div");
                                emojiPicker.tabIndex = 0, emojiInput.hasAttribute("data-meteor-emoji-large") ? (emojiPicker.style.zIndex = "999", emojiPicker.style.display = "block", emojiPicker.style.width = "100%", emojiPicker.style.marginBottom = "15px") : (emojiPicker.style.position = "absolute", emojiPicker.style.right = "15px", emojiPicker.style.top = "-250px", emojiPicker.style.display = "none", emojiPicker.style.width = "400px"), emojiPicker.style.zIndex = "999", emojiPicker.style.overflowY = "scroll", emojiPicker.style.height = "250px", emojiPicker.style.background = "#fff", emojiPicker.style.borderRadius = "5px", emojiPicker.style.boxShadow = "0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)", emojiPicker.style.borderRadius = "2px;", emojiPicker.style.marginTop = "5px", emojiPicker.style.outline = "none", emojiPicker.classList.add("emojiPicker");
                                var emojiTrigger = document.createElement("a");
                                emojiTrigger.style.position = "absolute", emojiTrigger.style.top = "14px", emojiTrigger.style.right = "15px", emojiTrigger.style.textDecoration = "none", emojiTrigger.setAttribute("href", "javascript:void(0)"), emojiTrigger.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 12 14"><path d="M8.9 8.4q-0.3 0.9-1.1 1.5t-1.8 0.6-1.8-0.6-1.1-1.5q-0.1-0.2 0-0.4t0.3-0.2q0.2-0.1 0.4 0t0.2 0.3q0.2 0.6 0.7 1t1.2 0.4 1.2-0.4 0.7-1q0.1-0.2 0.3-0.3t0.4 0 0.3 0.2 0 0.4zM5 5q0 0.4-0.3 0.7t-0.7 0.3-0.7-0.3-0.3-0.7 0.3-0.7 0.7-0.3 0.7 0.3 0.3 0.7zM9 5q0 0.4-0.3 0.7t-0.7 0.3-0.7-0.3-0.3-0.7 0.3-0.7 0.7-0.3 0.7 0.3 0.3 0.7zM11 7q0-1-0.4-1.9t-1.1-1.6-1.6-1.1-1.9-0.4-1.9 0.4-1.6 1.1-1.1 1.6-0.4 1.9 0.4 1.9 1.1 1.6 1.6 1.1 1.9 0.4 1.9-0.4 1.6-1.1 1.1-1.6 0.4-1.9zM12 7q0 1.6-0.8 3t-2.2 2.2-3 0.8-3-0.8-2.2-2.2-0.8-3 0.8-3 2.2-2.2 3-0.8 3 0.8 2.2 2.2 0.8 3z"/></svg>', emojiTrigger.onclick = function () {
                                    "none" === emojiPicker.style.display ? emojiPicker.style.display = "block" : "block" === emojiPicker.style.display && (emojiPicker.style.display = "none"), emojiPicker.focus()
                                }, emojiInput.hasAttribute("data-meteor-emoji-large") || emojiContainer.appendChild(emojiTrigger), window.addEventListener("click", function (e) {
                                    emojiInput.hasAttribute("data-meteor-emoji-large") || "block" === emojiPicker.style.display && (emojiPicker.contains(e.target) || emojiTrigger.contains(e.target) || (emojiPicker.style.display = "none"))
                                });
                                var facesCategory = document.createElement("ul");
                                facesCategory.style.padding = "10px 0px", facesCategory.style.margin = "0", facesCategory.style.marginLeft = "3%", facesCategory.style.flexWrap = "wrap", facesCategory.classList.add("faces");
                                var animalsCategory = document.createElement("ul");
                                animalsCategory.style.padding = "10px 0px", animalsCategory.style.margin = "0", animalsCategory.style.marginLeft = "3%", animalsCategory.style.flexWrap = "wrap", animalsCategory.classList.add("animals"), animalsCategory.style.display = "none";
                                var foodCategory = document.createElement("ul");
                                foodCategory.style.padding = "10px 0px", foodCategory.style.margin = "0", foodCategory.style.marginLeft = "3%", foodCategory.style.flexWrap = "wrap", foodCategory.classList.add("food"), foodCategory.style.display = "none";
                                var sportCategory = document.createElement("ul");
                                sportCategory.style.padding = "10px 0px", sportCategory.style.margin = "0", sportCategory.style.marginLeft = "3%", sportCategory.style.flexWrap = "wrap", sportCategory.classList.add("sport"), sportCategory.style.display = "none";
                                var transportCategory = document.createElement("ul");
                                transportCategory.style.padding = "10px 0px", transportCategory.style.margin = "0", transportCategory.style.marginLeft = "3%", transportCategory.style.flexWrap = "wrap", transportCategory.classList.add("transport"), transportCategory.style.display = "none";
                                var objectsCategory = document.createElement("ul");
                                objectsCategory.style.padding = "10px 0px", objectsCategory.style.margin = "0", objectsCategory.style.marginLeft = "3%", objectsCategory.style.flexWrap = "wrap", objectsCategory.classList.add("objects"), objectsCategory.style.display = "none";
                                var emojiCategory = document.createElement("ul");
                                emojiCategory.style.padding = "0px", emojiCategory.style.margin = "0", emojiCategory.style.display = "table", emojiCategory.style.width = "100%", emojiCategory.style.background = "#eff0f1", emojiCategory.style.listStyle = "none", emojiCategory.classList.add("category");
                                var emojiCategories = new Array;
                                emojiCategories.push({
                                    name: "faces",
                                    svg: '<svg id="faces" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="faces" d="M74.34,128.48a53.5,53.5,0,1,1,37.84-15.67,53.16,53.16,0,0,1-37.84,15.67Zm0-97.89a44.4,44.4,0,1,0,31.4,13,44.07,44.07,0,0,0-31.4-13Z"/><path id="faces" d="M74.35,108A33.07,33.07,0,0,1,41.29,75a2.28,2.28,0,0,1,2.27-2.28h0A2.27,2.27,0,0,1,45.83,75a28.52,28.52,0,0,0,57,0,2.27,2.27,0,0,1,4.54,0A33.09,33.09,0,0,1,74.35,108Z"/><path id="faces" d="M58.84,62a6.81,6.81,0,1,0,6.81,6.81A6.81,6.81,0,0,0,58.84,62Z"/><path id="faces" d="M89.87,62a6.81,6.81,0,1,0,6.81,6.81A6.82,6.82,0,0,0,89.87,62Z"/></svg>'
                                }), emojiCategories.push({
                                    name: "animals",
                                    svg: '<svg id="animals" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="animals" d="M59.9,91.75h0c-22.46,0-41.82-19.34-44.09-44A52.1,52.1,0,0,1,16,36.8a4.51,4.51,0,0,1,2.63-3.62,39.79,39.79,0,0,1,12.74-3.37c23.92-2.15,45.35,17.83,47.74,43.86a52.77,52.77,0,0,1-.15,10.93,4.56,4.56,0,0,1-2.64,3.62,39.67,39.67,0,0,1-12.73,3.36c-1.23.11-2.45.17-3.66.17ZM24.76,40.49a41.29,41.29,0,0,0,.09,6.4C26.7,67,42.09,82.66,59.9,82.67h0c.94,0,1.88,0,2.83-.14a30.39,30.39,0,0,0,7.41-1.62,41.14,41.14,0,0,0-.11-6.4C68.09,53.38,51.11,37.08,32.17,38.86a30.78,30.78,0,0,0-7.41,1.63Z"/><path id="animals" d="M36.68,125.64a4.53,4.53,0,0,1-4.33-3.17,53.32,53.32,0,0,1-2.26-11A50.42,50.42,0,0,1,39.51,76.6c7.35-9.91,17.84-16,29.5-17,1.16-.11,2.33-.13,3.47-.13a4.54,4.54,0,0,1,4.33,3.16,51.59,51.59,0,0,1,2.27,11.08,50.39,50.39,0,0,1-9.42,34.8c-7.35,9.91-17.83,16-29.5,17a17.63,17.63,0,0,1-3.48.12ZM69.09,68.69A32.41,32.41,0,0,0,46.8,82a42.57,42.57,0,0,0-6.71,34.38,32.38,32.38,0,0,0,22.28-13.32A41.35,41.35,0,0,0,70,74.51a39.38,39.38,0,0,0-.94-5.82Z"/><path id="animals" d="M90.27,91.75c-1.22,0-2.43-.06-3.66-.17a39.67,39.67,0,0,1-12.73-3.36,4.57,4.57,0,0,1-2.64-3.61,53.38,53.38,0,0,1-.17-10.93c2.41-26,23.7-46.07,47.76-43.87a39.74,39.74,0,0,1,12.73,3.37,4.57,4.57,0,0,1,2.64,3.62,53.35,53.35,0,0,1,.16,10.92c-2.28,24.69-21.65,44-44.09,44ZM80,80.91a30.57,30.57,0,0,0,7.42,1.62c19.07,1.78,35.92-14.53,37.87-35.64a42.55,42.55,0,0,0,.1-6.4A30.86,30.86,0,0,0,118,38.86C99,37.07,82.06,53.38,80.12,74.51a43.91,43.91,0,0,0-.1,6.4Z"/><path id="animals" d="M113.49,125.64h0c-1.16,0-2.3,0-3.46-.12-23.9-2.21-41.36-25.47-38.94-51.85A53.52,53.52,0,0,1,73.34,62.6a4.55,4.55,0,0,1,4.33-3.16c1.16,0,2.34,0,3.51.13,11.64,1.07,22.11,7.12,29.48,17a50.51,50.51,0,0,1,9.42,34.81,53.51,53.51,0,0,1-2.26,11,4.54,4.54,0,0,1-4.33,3.19ZM81.08,68.69a42.53,42.53,0,0,0-1,5.82c-1.94,21.1,11.45,39.71,29.95,41.88A42.38,42.38,0,0,0,103.36,82,32.42,32.42,0,0,0,81.08,68.69Z"/><path id="animals" d="M75.08,45.45a7.83,7.83,0,1,0,7.83,7.83,7.83,7.83,0,0,0-7.83-7.83Z"/><path id="animals" d="M76.29,51.89a2.26,2.26,0,0,1-2.14-3A46,46,0,0,1,92.82,25.34a2.27,2.27,0,1,1,2.4,3.86A41.4,41.4,0,0,0,78.43,50.39a2.28,2.28,0,0,1-2.14,1.5Z"/><path id="animals" d="M73.87,51.89a2.28,2.28,0,0,1-2.14-1.5A41.35,41.35,0,0,0,54.94,29.2a2.27,2.27,0,0,1,2.39-3.86A46,46,0,0,1,76,48.85a2.28,2.28,0,0,1-1.37,2.91,2.31,2.31,0,0,1-.77.13Z"/></svg>'
                                }), emojiCategories.push({
                                    name: "food",
                                    svg: '<svg id="food" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="food" d="M104,20.76h.15c15.83.52,24.08,21.48,24.07,32.56.26,12.42-10.72,23.55-24,24.21a3.53,3.53,0,0,1-.46,0c-13.25-.66-24.23-11.8-24-24.3,0-11,8.26-31.95,24.07-32.47Zm0,47.69c8.25-.54,15.3-7.51,15.14-15,0-8.12-6.22-23.1-15.14-23.57-8.9.46-15.14,15.45-15.14,23.48-.14,7.61,6.9,14.59,15.14,15.13Z"/><path id="food" d="M97.19,69.21h.14a4.53,4.53,0,0,1,4.4,4.68l-1.48,46.92a1.59,1.59,0,0,0,.5,1.06,4.6,4.6,0,0,0,3.25,1.19h0a4.57,4.57,0,0,0,3.26-1.2,1.53,1.53,0,0,0,.49-1l-1.48-46.95a4.54,4.54,0,1,1,9.08-.28l1.47,46.91a10.42,10.42,0,0,1-3,7.65,13.65,13.65,0,0,1-9.81,4h0a13.58,13.58,0,0,1-9.79-4,10.42,10.42,0,0,1-3-7.67l1.48-46.89a4.53,4.53,0,0,1,4.53-4.4Z"/><path id="food" d="M41.84,69.21H42a4.53,4.53,0,0,1,4.4,4.68L44.9,120.81a1.57,1.57,0,0,0,.5,1.06,4.6,4.6,0,0,0,3.25,1.19h0a4.51,4.51,0,0,0,3.24-1.19,1.48,1.48,0,0,0,.5-1L50.93,73.89a4.53,4.53,0,0,1,4.39-4.68A4.4,4.4,0,0,1,60,73.61l1.48,46.91a10.49,10.49,0,0,1-3,7.66,13.57,13.57,0,0,1-9.78,4h0a13.59,13.59,0,0,1-9.78-4,10.48,10.48,0,0,1-3-7.67l1.48-46.9a4.54,4.54,0,0,1,4.54-4.4Z"/><path id="food" d="M28.59,20.76a4.54,4.54,0,0,1,4.54,4.54V51a15.52,15.52,0,0,0,31,0V25.3a4.55,4.55,0,0,1,9.09,0V51a24.61,24.61,0,1,1-49.21,0V25.3a4.54,4.54,0,0,1,4.54-4.54Z"/><path id="food" d="M55.34,20.76a4.54,4.54,0,0,1,4.54,4.54v19a4.54,4.54,0,1,1-9.08,0v-19a4.54,4.54,0,0,1,4.54-4.54Z"/><path id="food" d="M42,20.76a4.54,4.54,0,0,1,4.54,4.54v19a4.54,4.54,0,1,1-9.08,0v-19A4.54,4.54,0,0,1,42,20.76Z"/></svg>'
                                }), emojiCategories.push({
                                    name: "sport",
                                    svg: '<svg id="sport" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="sport" d="M75.35,130.24a53.49,53.49,0,1,1,53.48-53.49,53.55,53.55,0,0,1-53.48,53.49Zm0-97.89a44.41,44.41,0,1,0,44.4,44.4,44.1,44.1,0,0,0-44.4-44.4Z"/><path id="sport" d="M119.24,84.08A51.29,51.29,0,0,1,68,32.86a49.44,49.44,0,0,1,.26-5,2.26,2.26,0,0,1,2-2c1.66-.16,3.34-.25,5-.25a51.26,51.26,0,0,1,51.21,51.21c0,1.71-.09,3.38-.25,5a2.28,2.28,0,0,1-2,2c-1.65.16-3.33.25-5,.25ZM72.64,30.16c-.06.9-.08,1.79-.08,2.7a46.73,46.73,0,0,0,46.68,46.68q1.37,0,2.7-.09c.06-.89.08-1.79.08-2.7A46.72,46.72,0,0,0,75.35,30.08c-.91,0-1.82,0-2.71.08Z"/><path id="sport" d="M75.35,128A51.28,51.28,0,0,1,24.12,76.76c0-1.7.1-3.38.25-5a2.29,2.29,0,0,1,2-2c1.66-.16,3.33-.25,5.05-.25a51.27,51.27,0,0,1,51.21,51.22c0,1.69-.09,3.37-.25,5a2.27,2.27,0,0,1-2,2c-1.66.16-3.32.25-5,.25ZM28.75,74.05c-.05.9-.09,1.8-.09,2.71a46.74,46.74,0,0,0,46.69,46.67c.91,0,1.8,0,2.7-.08,0-.9.08-1.8.08-2.7A46.73,46.73,0,0,0,31.46,74c-.91,0-1.81,0-2.71.08Z"/><polygon id="sport" points="42.69 112.61 39.48 109.4 108 40.88 111.21 44.1 42.69 112.61 42.69 112.61"/></svg>'
                                }), emojiCategories.push({
                                    name: "transport",
                                    svg: '<svg id="transport" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="transport" d="M120.7,116H31a4.55,4.55,0,0,1-4.54-4.55V54.28A31.82,31.82,0,0,1,58.25,22.49h35.2a31.83,31.83,0,0,1,31.8,31.79v57.15A4.55,4.55,0,0,1,120.7,116Zm-85.16-9.09h80.62V54.28A22.74,22.74,0,0,0,93.45,31.57H58.25A22.74,22.74,0,0,0,35.54,54.28v52.61Z"/><path id="transport" d="M49.35,129.23c-8.53,0-13.62-2.77-13.62-7.41V115.6a4.54,4.54,0,1,1,9.08,0v4.06a21.32,21.32,0,0,0,9.09,0V115.6a4.54,4.54,0,0,1,9.08,0v6.22c0,4.64-5.09,7.41-13.63,7.41Z"/><path id="transport" d="M102.34,129.23c-8.53,0-13.62-2.77-13.62-7.41V115.6a4.54,4.54,0,0,1,9.08,0v4.06a21.28,21.28,0,0,0,9.08,0V115.6a4.55,4.55,0,0,1,9.09,0v6.22c0,4.64-5.09,7.41-13.63,7.41Z"/><path id="transport" d="M97.81,44.83H53.9a4.55,4.55,0,1,1,0-9.09H97.81a4.55,4.55,0,0,1,0,9.09Z"/><path id="transport" d="M54.28,84.2A6.8,6.8,0,1,0,61.07,91a6.8,6.8,0,0,0-6.79-6.8Z"/><path id="transport" d="M97.43,84.2a6.8,6.8,0,1,0,6.79,6.8,6.8,6.8,0,0,0-6.79-6.8Z"/><path id="transport" d="M107.08,81H44.63a6.82,6.82,0,0,1-6.82-6.82V54.28a6.82,6.82,0,0,1,6.82-6.81h62.45a6.82,6.82,0,0,1,6.81,6.81V74.15A6.83,6.83,0,0,1,107.08,81ZM44.63,52a2.28,2.28,0,0,0-2.28,2.27V74.15a2.28,2.28,0,0,0,2.28,2.27h62.45a2.27,2.27,0,0,0,2.27-2.27V54.28A2.27,2.27,0,0,0,107.08,52Z"/></svg>'
                                }), emojiCategories.push({
                                    name: "objects",
                                    svg: '<svg id="objects" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 150 150"><path id="objects" d="M107.78,129a4.55,4.55,0,0,1-2.67-.87l-30-21.79-30,21.79a4.53,4.53,0,0,1-5.34,0,4.58,4.58,0,0,1-1.65-5.08L49.59,87.82,19.6,66a4.54,4.54,0,0,1,2.67-8.22H59.34L70.8,22.55a4.55,4.55,0,0,1,8.64,0L90.89,57.81H128A4.54,4.54,0,0,1,130.63,66l-30,21.79,11.46,35.25a4.55,4.55,0,0,1-4.32,6ZM75.12,96.2a4.53,4.53,0,0,1,2.67.87l21.35,15.51L91,87.49a4.55,4.55,0,0,1,1.65-5.08L114,66.89H87.59a4.54,4.54,0,0,1-4.32-3.13l-8.15-25.1L67,63.76a4.53,4.53,0,0,1-4.32,3.13H36.25L57.61,82.41a4.54,4.54,0,0,1,1.65,5.08l-8.17,25.09L72.45,97.07a4.53,4.53,0,0,1,2.67-.87Z"/></svg>'
                                });
                                emojiCategories.map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.padding = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.style.display = "table-cell", emojiLink.style.textAlign = "center", emojiLink.id = String(item.name), "faces" == String(item.name) && (emojiLink.style.background = "#c2c2c2"), emojiLink.innerHTML = String(item.svg), emojiLink.onmousedown = clickCategory, emojiCategory.appendChild(emojiLink)
                                }), [128512, 128513, 128514, 129315, 128515, 128516, 128517, 128518, 128521, 128522, 128523, 128526, 128525, 128536, 128535, 128537, 128538, 128578, 129303, 129300, 128528, 128529, 128566, 128580, 128527, 128547, 128549, 128558, 129296, 128559, 128554, 128555, 128564, 128524, 129299, 128539, 128540, 128541, 129316, 128530, 128531, 128532, 128533, 128579, 129297, 128562, 128577, 128534, 128542, 128543, 128548, 128546, 128557, 128550, 128551, 128552, 128553, 128556, 128560, 128561, 128563, 128565, 128545, 128544, 128519, 129312, 129313, 129317, 128567, 129298, 129301, 129314, 129319, 128520, 128127, 128121, 128122, 128128, 128123, 128125, 128126, 129302, 128169, 128570, 128568, 128569, 128571, 128572, 128573, 128576, 128575, 128574, 128584, 128585, 128586, 128102, 128103, 128104, 128105, 128116, 128117, 128118, 128124, 128110, 128373, 128130, 128119, 128115, 128113, 127877, 129334, 128120, 129332, 128112, 129333, 129328, 128114, 128589, 128590, 128581, 128582, 128129, 128587, 128583, 129318, 129335, 128134, 128135, 128694, 127939, 128131, 128378, 128111, 128372, 128107, 128108, 128109, 128143, 128105, 128104, 128105, 128145, 128106, 128170, 129331, 128072, 128073, 9757, 128070, 128405, 128071, 9996, 129310, 128406, 129304, 129305, 128400, 9995, 128076, 128077, 128078, 9994, 128074, 129307, 129308, 129306, 128075, 128079, 9997, 128080, 128588, 128591, 129309, 128133, 128066, 128067, 128099, 128064, 128065, 128069, 128068, 128139, 128152, 10084, 128147, 128148, 128149, 128150, 128151, 128153, 128154, 128155, 128156, 128420, 128157, 128158, 128159, 128140, 128164, 128162, 128163, 128165, 128166, 128168, 128171, 128172, 128488, 128495, 128173, 128371].map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, facesCategory.appendChild(emojiLink)
                                }), [128053, 128018, 129421, 128054, 128021, 128041, 128058, 129418, 128049, 128008, 129409, 128047, 128005, 128006, 128052, 128014, 129420, 129412, 128046, 128002, 128003, 128004, 128055, 128022, 128023, 128061, 128015, 128017, 128016, 128042, 128043, 128024, 129423, 128045, 128001, 128000, 128057, 128048, 128007, 128063, 129415, 128059, 128040, 128060, 128062, 129411, 128020, 128019, 128035, 128036, 128037, 128038, 128039, 128330, 129413, 129414, 129417, 128056, 128010, 128034, 129422, 128013, 128050, 128009, 128051, 128011, 128044, 128031, 128032, 128033, 129416, 128025, 128026, 129408, 129424, 129425, 129419, 128012, 128027, 128028, 128029, 128030, 128375, 128376, 129410, 128144, 127800, 128174, 127989, 127801, 129344, 127802, 127803, 127804, 127799, 127793, 127794, 127795, 127796, 127797, 127806, 127807, 9752, 127808, 127809, 127810, 127811].map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, animalsCategory.appendChild(emojiLink)
                                }), [127815, 127816, 127817, 127818, 127819, 127820, 127821, 127822, 127823, 127824, 127825, 127826, 127827, 129373, 127813, 129361, 127814, 129364, 129365, 127805, 127798, 129362, 127812, 129372, 127792, 127838, 129360, 129366, 129374, 129472, 127830, 127831, 129363, 127828, 127839, 127829, 127789, 127790, 127791, 129369, 129370, 127859, 129368, 127858, 129367, 127871, 127857, 127832, 127833, 127834, 127835, 127836, 127837, 127840, 127842, 127843, 127844, 127845, 127841, 127846, 127847, 127848, 127849, 127850, 127874, 127856, 127851, 127852, 127853, 127854, 127855, 127868, 129371, 9749, 127861, 127862, 127870, 127863, 127864, 127865, 127866, 127867, 129346, 129347, 127869, 127860, 129348, 128298].map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, foodCategory.appendChild(emojiLink)
                                }), [127903, 127915, 127894, 127942, 127941, 129351, 129352, 129353, 9917, 9918, 127936, 127952, 127944, 127945, 127934, 127921, 127923, 127951, 127953, 127954, 127955, 127992, 129354, 129355, 129349, 127919, 9971, 9976, 127907, 127933, 127935, 129338, 127943, 9975, 127938, 127948, 127940, 128675, 127946, 9977, 127947, 128692, 128693, 129336, 129340, 129341, 129342, 127995, 129337, 127995, 127918, 128377, 127922, 9824, 9829, 9830, 9827, 127183, 126980, 127924].map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, sportCategory.appendChild(emojiLink)
                                }), [127994, 127757, 127758, 127759, 127760, 128506, 128510, 127956, 9968, 127755, 128507, 127957, 127958, 127964, 127965, 127966, 127967, 127963, 127959, 127960, 127961, 127962, 127968, 127969, 127970, 127971, 127972, 127973, 127974, 127976, 127977, 127978, 127979, 127980, 127981, 127983, 127984, 128146, 128508, 128509, 9962, 128332, 128333, 9961, 128331, 9970, 9978, 127745, 127747, 127748, 127749, 127750, 127751, 127753, 9832, 127756, 127904, 127905, 127906, 128136, 127914, 127917, 128444, 127912, 127920, 128642, 128643, 128644, 128645, 128646, 128647, 128648, 128649, 128650, 128669, 128670, 128651, 128652, 128653, 128654, 128656, 128657, 128658, 128659, 128660, 128661, 128662, 128663, 128664, 128665, 128666, 128667, 128668, 128690, 128756, 128757, 127950, 127949, 128655, 128739, 128740, 9981, 128680, 128677, 128678, 128679, 128721, 9875, 9973, 128758, 128676, 128755, 9972, 128741, 128674, 9992, 128745, 128747, 128748, 128186, 128641, 128671, 128672, 128673, 128640, 128752, 128718, 128682, 128716, 128719, 128715, 128701, 128703, 128704, 128705, 8987, 9203, 8986, 9200, 9201, 9202, 128368, 128347, 128359, 128336, 128348, 128337, 128349, 128338, 128350, 128339, 128351, 128340, 128352, 128341, 128353, 128342, 128354, 128343, 128355, 128344, 128356, 128345, 128357, 128346, 128358, 127761, 127762, 127763, 127764, 127765, 127766, 127767, 127768, 127769, 127770, 127771, 127772, 127777, 9728, 127773, 127774, 11088, 127775, 127776, 9729, 9925, 9928, 127780, 127781, 127782, 127783, 127784, 127785, 127786, 127787, 127788, 127744, 127752, 127746, 9730, 9748, 9969, 9889, 10052, 9731, 9924].map(function (item) {
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, transportCategory.appendChild(emojiLink)
                                }), [128263, 128264, 128265, 128266, 128226, 128227, 128239, 128276, 128277, 127932, 127925, 127926, 127897, 127898, 127899, 127908, 127911, 128251, 127927, 127928, 127929, 127930, 127931, 129345, 128241, 128242, 9742, 128222, 128223, 128224, 128267, 128268, 128187, 128421, 128424, 9000, 128433, 128434, 128189, 128190, 128191, 128192, 127909, 127902, 128253, 127916, 128250, 128247, 128248, 128249, 128252, 128269, 128270, 128300, 128301, 128225, 128367, 128161, 128294, 127982, 128212, 128213, 128214, 128215, 128216, 128217, 128218, 128211, 128210, 128195, 128220, 128196, 128240, 128478, 128209, 128278, 127991, 128176, 128180, 128181, 128182, 128183, 128184, 128179, 128185, 128177, 128178, 9993, 128231, 128232, 128233, 128228, 128229, 128230, 128235, 128234, 128236, 128237, 128238, 128499, 9999, 10002, 128395, 128394, 128396, 128397, 128221, 128188, 128193, 128194, 128450, 128197, 128198, 128466, 128467, 128199, 128200, 128201, 128202, 128203, 128204, 128205, 128206, 128391, 128207, 128208, 9986, 128451, 128452, 128465, 128274, 128275, 128271, 128272, 128273, 128477, 128296, 9935, 9874, 128736, 128481, 9876, 128299, 127993, 128737, 128295, 128297, 9881, 128476, 9879, 9878, 128279, 9939, 128137, 128138, 128684, 9904, 9905, 128511, 128738, 128302, 128722, 127975, 128686, 128688, 9855, 128697, 128698, 128699, 128700, 128702, 128706, 128707, 128708, 128709, 9888, 128696, 9940, 128683, 128691, 128685, 128687, 128689, 128695, 128245, 128286, 9762, 9763, 11014, 8599, 10145, 8600, 11015, 8601, 11013, 8598, 8597, 8596, 8617, 8618, 10548, 10549, 128259, 128260, 128281, 128282, 128283, 128284, 128285, 128720, 9883, 128329, 10017, 9784, 9775, 10013, 9766, 9770, 9774, 128334, 128303, 9851, 128219, 9884, 128304, 128305, 11093, 9989, 9745, 10004, 10006, 10060, 10062, 10133, 10134, 10135, 10160, 10175, 12349, 10035, 10036, 10055, 8252, 8265, 10067, 10068, 10069, 10071, 12336, 169, 174, 8482, 9800, 9801, 9802, 9803, 9804, 9805, 9806, 9807, 9808, 9809, 9810, 9811, 9934, 128256, 128257, 128258, 9654, 9193, 9197, 9199, 9664, 9194, 9198, 128316, 9195, 128317, 9196, 9208, 9209, 9210, 9167, 127910, 128261, 128262, 128246, 128243, 128244, 128287, 128175, 128288, 128289, 128290, 128291, 128292, 127344, 127374, 127345, 127377, 127378, 127379, 8505, 127380, 9410, 127381, 127382, 127358, 127383, 127359, 127384, 127385, 127386, 127489, 127490, 127543, 127542, 127535, 127568, 127545, 127514, 127538, 127569, 127544, 127540, 127539, 12951, 12953, 127546, 127541, 9642, 9643, 9723, 9724, 9725, 9726, 11035, 11036, 128310, 128311, 128312, 128313, 128314, 128315, 128160, 128280, 128306, 128307, 9898, 9899, 128308, 128309, 127937, 128681, 127884, 127988, 127987].map(function (item) {
                                    var emojiLi = document.createElement("li");
                                    emojiLi.style.display = "inline-block", emojiLi.style.margin = "5px";
                                    var emojiLink = document.createElement("a");
                                    emojiLink.style.textDecoration = "none", emojiLink.style.margin = "5px", emojiLink.style.position = "initial", emojiLink.style.fontSize = "24px", emojiLink.setAttribute("href", "javascript:void(0)"), emojiLink.innerHTML = String.fromCodePoint(item), emojiLink.onmousedown = clickLink, objectsCategory.appendChild(emojiLink)
                                }), emojiPicker.appendChild(emojiCategory), emojiPicker.appendChild(facesCategory), emojiPicker.appendChild(animalsCategory), emojiPicker.appendChild(foodCategory), emojiPicker.appendChild(sportCategory), emojiPicker.appendChild(transportCategory), emojiPicker.appendChild(objectsCategory), emojiContainer.appendChild(emojiPicker)
                            }
                        }]), MeteorEmoji
                    }();
                module.exports = MeteorEmoji
            })
        }, {}]
    }, {}, [1])(1)
});