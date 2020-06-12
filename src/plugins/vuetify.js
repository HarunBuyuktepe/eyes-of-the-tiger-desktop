import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/dist/vuetify.min.css'
Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false,
    themes: {
      light: {
        primary: '#5D4037',
        secondary: '#543c34',
        accent: '#F57C00',
        error: '#d50000',
      },
      // dark: {
      //   primary: '#424242',
      //   secondary: '#102027',
      //   accent: '#0288d1',
      //   error: '#d50000',
      // }
    }
  },
  icons: {
    iconfont: 'md',
  },
});
