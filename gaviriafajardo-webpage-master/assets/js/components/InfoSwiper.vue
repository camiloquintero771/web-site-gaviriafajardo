<template>
  <div class="info-swiper px-xxl-6 pt-5 pb-2">
    <span class="info-swiper__title text-white fw-bold bg-primary display-4 px-2 py-0">{{ title }}</span>
    <div class="d-flex justify-content-center align-items-center my-5">
    <div class="swiper-button-prev">
      <i class="bi bi-chevron-left text-secondary display-3 cursor-pointer"></i>
    </div>
    <swiper
      :slidesPerView="1"
      :spaceBetween="50"
      :loop="false"
      :simulateTouch="false"
      :loopFillGroupWithBlank="false"
      :breakpoints="breakpoints"
      :modules="modules"
      :navigation="navigation"
      class="swiper w-100"
    >
        <swiper-slide class="d-flex justify-content-center align-items-center" v-for="news in list_news" :key="news">
          <news-card
            :image="news.img"
            :text-small="news.text_small"
            :text-bold="news.text_bold"
            :description="news.description"
            :href="news.url"
          >
          </news-card>
        </swiper-slide>
    </swiper>
    <div class="swiper-button-next">
      <i class="bi bi-chevron-right text-secondary display-3 cursor-pointer"></i>
    </div>
    </div>
  </div>
</template>

<script>
import { Swiper } from 'swiper/vue/swiper';
import { SwiperSlide } from 'swiper/vue/swiper-slide';
import { Navigation } from 'swiper';
import NewsCard from "@/js/components/NewsCard";


export default {
  name: "BlurredCarousel",
  components: {NewsCard, Swiper, SwiperSlide},

  props:{
    title:{
      type:String,
      required:true
    },
    list_news:{
      type:Array,
      required:true
    }
  },

  data() {
    return {
      breakpoints: {
        1400: {
          slidesPerView: 4,
          spaceBetween: 10,
        },
        1200: {
          slidesPerView: 3,
          spaceBetween: 10,
        },
        992: {
          slidesPerView: 3,
          spaceBetween: 10,
        },
        768:{
          slidesPerView: 2,
          spaceBetween: 40,
        },
        576: {
          slidesPerView: 1,
          spaceBetween: 40,
        },
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      modules: [Navigation],
    };
  },
}
</script>

<style lang="scss">
@import '~swiper/swiper.scss';

.info-swiper{
  box-shadow: 0px 0px 20px #00000029;
  width: 100%;
  position: relative;
  &__title{
    border-radius: 15px;
  }
}
</style>
