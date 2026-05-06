<template>
  <div class="detail-swiper text-center pt-5 pb-2 px-2">
    <h5 class="text-secondary fw-bold pt-3 pb-0 mb-0">{{ title }}</h5>
    <div class="line_title_long m-0 mx-auto"></div>
    <div class="d-flex justify-content-center align-items-center my-5">
    <div class="swiper-button-prev bg-gray rounded-3">
      <i class="bi bi-chevron-left text-white display-6  cursor-pointer"></i>
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
        <swiper-slide class="d-flex justify-content-center align-items-center" v-for="card in cards" :key="news">
          <div class="card d-flex flex-column align-items-center justify-content-center pt-3">
            <img :src="card.img" class="card__image mx-auto">
            <h5 class="text-secondary fw-bold my-2">{{ card.title }}</h5>
            <a type="button" class="btn btn_basic fw-bold px-2" :href="card.url">Ver más...</a>
          </div>
        </swiper-slide>
    </swiper>
    <div class="swiper-button-next bg-gray rounded-3">
      <i class="bi bi-chevron-right text-white display-6 cursor-pointer"></i>
    </div>
    </div>
  </div>
</template>

<script>
import { Swiper } from 'swiper/vue/swiper';
import { SwiperSlide } from 'swiper/vue/swiper-slide';
import { Navigation } from 'swiper';

export default {
  name: "DetailSwiper",
  components: { Swiper, SwiperSlide},

  props:{
    title:{
      type:String,
      required:true
    },
    cards:{
      type:Array,
      required:true
    }
  },

  data() {
    return {
      breakpoints: {
        1400: {
          slidesPerView: 4,
          spaceBetween: 50,
        },
        1200: {
          slidesPerView: 4,
          spaceBetween: 10,
        },
        992: {
          slidesPerView: 4,
          spaceBetween: 10,
        },
        768:{
          slidesPerView: 3,
          spaceBetween: 10,
        },
        576: {
          slidesPerView: 2,
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
.detail-swiper{
  .card{
    border:none;
    width: 15rem;
    &__image{
      width: 100%;
      height: 170px;
      object-fit: cover;
      object-position: center;
      border-radius: 25px;
      box-shadow: 0px 0px 20px #00000029;
    }
  }
}
</style>
