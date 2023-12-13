# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!--next-version-placeholder-->

## v0.2.0 (2023-12-13)
### Feature
* ✨ Add CustomFields for System of Record information. ([`62486fd`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/62486fd03291d4f438f5c312354e807cbd008d41))
* ✨ Add LocationType DiffSyncModel. ([`4424aae`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/4424aaef8a258b61b6d6895577f1e1a194f75b96))
* ✨ Add function to retrieve Site information from UniFi. ([`9744864`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/97448647cf6eb95fc98c6d8c76844b9df2fd0805))
* ✨ Add UniFiAdapter with load functions. ([`fe8bf32`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/fe8bf32dcf8031adba1d8c796622c573d95cc02b))
* ✨ Update NautobotAdapter to be UniFiNautobotAdapter and specify top_level and models. ([`b2f6401`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/b2f640189987c0af3efcd5fbdc3cb7878fae9553))
* ✨ Add UniFi CRUD models. ([`3bdabb0`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/3bdabb06059105632fa6f7a173dae1cc4f933a73))
* ✨ Make base DiffSync models based off NautobotModel. ([`b8cb143`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/b8cb1432f761bbbb647c6abf9464a98033be6a9d))
* ✨ Add function to connect to UniFi controller to make API calls. ([`6be8a65`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/6be8a65008caeb073e298093dc8221173902fc0a))
* ✨ Add DEVICETYPE_MAP to match model code to full model name. ([`a52a31d`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/a52a31de371cc98899da6147ec1fbaeca978fb1a))

### Fix
* 🐛 Update loading to use updated class attributes from DiffSync models. ([`f973309`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/f973309d5be6aedf01ea67748e925e7767bdd324))
* 🐛 Update top_level to include missing models ([`fb22ac5`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/fb22ac5fc69407a70815cb82d0ab114fb691c74e))
* 🐛 Enable import only model flag for Role model ([`c37c3f3`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/c37c3f3e70e5f0c083d031ff390c51c94790ea6d))
* 🐛 Correct DeviceType attribute on Device to be device_type ([`4cb0109`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/4cb0109a6a5522339e287f8403eb78922e0b54d1))
* 🐛 Add Status to required objects in DiffSync models. ([`966ae84`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/966ae845d486c2f8c323fb3a0f64240fcdb5e434))
* 🐛 Update ContentType attributes to use TypeDict pattern. ([`166d551`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/166d55128270b68b57510a7c67fad12b1005dd61))
* 🐛 Fix variable name ([`0f1bf1c`](https://github.com/jdrew82/nautobot-app-ssot-unifi/commit/0f1bf1c9d426d5a3cc0bdf634c0e638b6852d40f))
