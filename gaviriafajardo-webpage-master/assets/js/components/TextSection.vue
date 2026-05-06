<template>
  <div class="text-section py-5 py-sm-6 py-md-5">
    <div class="row px-5 px-sm-6 px-xxl-7">
      <div :class="{ 'col-12': true, 'col-md-6': renderImage(), 'col-md-12': !renderImage(), 'my-auto text-start section-info': true }">
        <h3 class="text-primary fw-bold ">{{ titleSmall }}</h3>
        <h1 class="text-primary display-5 fw-bold"> {{ titleBig }}</h1>
        <div class="line_title my-2 "></div>
        <p class="fw-bold text-secondary py-2"  v-html="description"></p>
        <a v-if="showButton" type="button" class="btn btn_basic fw-bold px-3" :href="url">Ver más...</a>
      </div>
       <div v-if="renderImage()" class="col-12 col-md-6 my-auto section-image pt-5 pt-md-0">
        <img :src="image" class="text-section__image">
      </div>
    </div>
  </div>

</template>

<script>
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function startScroll() {
  return gsap.timeline({
    scrollTrigger: {
      trigger: '.text-section',
      start: 'top center',
      end: 'center center',
      scrub: true,
    },
  });
}

function endScroll() {
  return gsap.timeline({
    scrollTrigger: {
      trigger: '.text-section',
      start: 'center top',
      end: 'bottom top',
      scrub: true,
    },
  });
}

export default {
  name: "TextSection",

  props:{
    animation:{
      type:Boolean,
      required:true
    },
    showButton:{
      type:Boolean,
      required:true
    },
    titleSmall:{
      type:String,
      required:true
    },
    titleBig:{
      type:String,
      required:true
    },
    description:{
      type:String,
      required:true
    },
    image:{
      type:String,
      required:true
    },
    url:{
      type:String,
      required:true,
    }
  },

  mounted() {
    if (this.animation) {
      startScroll().fromTo('.section-info', { y: 600, x: -600, duration: 1 }, { y: 0, x: 0, duration: 1});
      startScroll().fromTo('.section-image', { y: 600, x: 600, duration: 1 }, { y: 0, x: 0, duration: 1});
      endScroll().to('.section-info', {y:-400, x:-600, duration:1});
      endScroll().to('.section-image', {y:-400, x:600, duration:1})
    }
  },
  methods:{
    renderImage(){
      if(this.image === ""){
        return false;
      }
      return true;
    },
  }

}
</script>

<style lang="scss">
.text-section{
  &__image{
    width: 100%;
    height: auto;
    object-fit: cover;
    object-position: center;
    border-radius: 30px;
    box-shadow: 0px 0px 30px #00000029;

    @media screen and (min-width:1200px ){
      height: 550px
    }
  }
}
</style>
