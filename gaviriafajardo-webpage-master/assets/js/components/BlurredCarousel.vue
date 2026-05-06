<template>
  <div class="blurred-carousel">
    <span class="text-primary fw-bold display-3">{{ title }}</span>
    <div class="d-flex justify-content-center align-items-center">
    <div class="blurred-carousel-prev">
      <i class="bi bi-chevron-left text-secondary display-3 cursor-pointer"></i>
    </div>
    <swiper
      :simulateTouch="false"
      :centered-slides="true"
      :loop="true"
      :breakpoints="breakpoints"
      :modules="modules"
      :navigation="navigation"
      class="swiper"
    >
        <swiper-slide v-for="service in services" :key="service" >
          <div class="d-flex flex-column  justify-content-center  align-items-center">
            <a class="text-decoration-none d-flex justify-content-center align-items-center" :href="service.url">
              <img :src="service.img" class="swiper__img" alt="...">
            </a>
            <span class="text-secondary fw-bold display-6 service_title">{{ service.title }}</span>
          </div>
        </swiper-slide>
    </swiper>
    <div class="blurred-carousel-next">
      <i class="bi bi-chevron-right text-secondary display-3 cursor-pointer"></i>
    </div>
    </div>
  </div>
</template>

<script>
import { Swiper } from 'swiper/vue/swiper';
import { SwiperSlide } from 'swiper/vue/swiper-slide';
import { Navigation } from 'swiper';


export default {
  name: "BlurredCarousel",
  components: {Swiper, SwiperSlide},

  props:{
    title:{
      type:String,
      required:true
    },
    services:{
      type:Array,
      required:true
    }
  },

  data() {
    return {
      breakpoints: {
        745: {
          slidesPerView: 3,
          spaceBetween: 0,
        },
        576: {
          slidesPerView: 1,
          spaceBetween: 0,
        },
      },
      navigation: {
        nextEl: '.blurred-carousel-next',
        prevEl: '.blurred-carousel-prev',
      },
      modules: [Navigation],
    };
  },
}
</script>

<style lang="scss">
@import '~swiper/swiper.scss';
.blurred-carousel {
  .swiper-slide {
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0px;
    background: transparent;
    transition: all .3s ease;
    opacity: 0.2;

    span {
      display: none;
      visibility: hidden;
    }

    img {
      display: block;
      width: 280px;
      height: 280px;
      border-radius: 50%;
      object-fit: cover;
      object-position: center;

      @media screen and (max-width: 1200px) {
        width: 250px;
        height: 250px;
      }

      @media screen and (max-width: 992px) {
        width: 230px;
        height: 230px;
      }
      @media screen and (max-width: 840px) {
        width: 200px;
        height: 200px;
      }

      @media screen and (max-width: 745px) {
        width: 250px;
        height: 250px;
      }
      @media screen and (max-width: 475px) {
        width: 170px;
        height: 170px;
      }
    }

    &.swiper-slide-active {
      color: #fff;
      transform: scale(1.4);
      z-index: 2;
      opacity: 1;
      background: transparent;

      span {
        display: block;
        visibility: visible;
      }

    }
  }

  .swiper {
    height: 600px;
    width: 70%;

    @media screen and (max-width: 1200px) {
      width: 100%;
    }
  }

  .service_title{
    @media screen and (max-width:796px) {
      font-size:30px;
      width:90%;
    }
  }
}
</style>
