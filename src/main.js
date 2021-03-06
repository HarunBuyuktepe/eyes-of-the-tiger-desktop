import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import resource from "vue-resource";
import store from "./store/store";
import VueCoreVideoPlayer from 'vue-core-video-player'
Vue.use(VueCoreVideoPlayer)

Vue.use(resource);

Vue.config.productionTip = false;

Vue.http.interceptors.push((request) => {
	// eslint-disable-next-line no-console
	request.headers.set("UserName", "harun");
	request.headers.set("Content-Type", "application/json");
	console.log(
		"REQUEST: "
			.concat(request.url)
			.concat(" | ")
			.concat(request.method)
	);
	console.log(request.headers);
});

new Vue({
	vuetify,
	router,
	store,
	render: (h) => h(App),
}).$mount("#app");
