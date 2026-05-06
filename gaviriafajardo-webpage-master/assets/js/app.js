import "../scss/app.scss";
import "../css/table.css";

import { createApp } from 'vue/dist/vue.esm-bundler';

import GoogleMapLoader from '@/js/components/GoogleMapLoader';
import GeneralCover from "@/js/components/GeneralCover";
import BlurredCarousel from "@/js/components/BlurredCarousel";
import InfoSwiper from "@/js/components/InfoSwiper";
import NewsCard from "@/js/components/NewsCard";
import TextSection from "@/js/components/TextSection";
import FormContact from "@/js/components/FormContact"
import DetailSwiper from "@/js/components/DetailSwiper";
import Table from "@/js/components/Table";

const Root = {
  delimiters: ['[[', ']]'],
  data() {
    return {
      // Some data
    };
  },
  mounted() {
    // Some code
  },
  methods: {
    // Some methods
  },
};

const app = createApp(Root);

app.component('google-map-loader', GoogleMapLoader)
app.component('general-cover', GeneralCover)
app.component('blurred-carousel', BlurredCarousel)
app.component('info-swiper',InfoSwiper)
app.component('news-card',NewsCard)
app.component('text-section',TextSection)
app.component('form-contact', FormContact)
app.component('detail-swiper',DetailSwiper)
app.component('table-vue',Table)

app.mount('#app');
