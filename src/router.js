import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from "./components/Home";
// import Information from "./components/pages/Information.vue"
// import HowToUse from "./components/pages/HowToUse";
// import EyesOfTheTigerTeam from "./components/pages/EyesOfTheTigerTeam";
Vue.use(VueRouter)


export default new VueRouter ({
    routes: [
        {
            path: "/",
            component: Home,
            name: "home"
        }
        // {
        //     path: "/Information",
        //     component: Information,
        //     name: "Information"
        // },
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
    ]
})
