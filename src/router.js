import Vue from "vue";
import VueRouter from "vue-router";
import Login from "./components/auth/Login.vue";
import Home from "./components/pages/Home";
import Settings from "./components/pages/Settings.vue";
import AboutUs from "./components/pages/AboutUs";
// import Information from "./components/pages/Information.vue"
// import HowToUse from "./components/pages/HowToUse";
// import EyesOfTheTigerTeam from "./components/pages/EyesOfTheTigerTeam";
Vue.use(VueRouter);

export default new VueRouter({
	routes: [
		{
			path: "/",
			component: Login,
			name: "Login",
		},
		{
			path: "/Home/:username",
			component: Home,
			name: "Home",
		},
		{
			path: "/Settings/:username",
			component: Settings,
			name: "Settings",
		},
		{
			path: "/AboutUs",
			component: AboutUs,
			name: "AboutUs",
		},
		// {
		//     path: "/HowToUse",
		//     component: HowToUse,
		//     name: "HowTUse"
		// },
		// {
		//     path: "/EyesOfTheTigerTeam",
		//     component: EyesOfTheTigerTeam,
		//     name: "EyesOfTheTigerTeam"
		// }
	],
	mode: "history",
});
