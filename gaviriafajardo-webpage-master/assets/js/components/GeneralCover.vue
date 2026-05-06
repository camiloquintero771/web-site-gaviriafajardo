<template>
  <div class="general-cover text-white w-100 overflow-hidden fit z-index-1n">
    <div id="general-cover-carousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img :src="this.img" class="d-block general-cover__img" alt="...">
        </div>
        <div class="carousel-item" v-for="(image,i) in images" :key="i">
          <img :src="image" class="d-block general-cover__img" alt="...">
        </div>
      </div>
    </div>
  </div>
  <div class="cover-text text-white w-100 d-flex justify-content-center">
    <h1 class="text_shadow text-center w-75 medium-size align-items-center">{{ text }}<br>
      <span class="fw-bold h1 big-size text_shadow text-uppercase">{{ textBold }}</span>
    </h1>
  </div>
  <div v-if="showButton" class="cover-button d-flex justify-content-center">
    <button type="button" class="btn btn_cover fw-bold px-5 px-sm-4" @click="contactClick()">Contáctanos</button>
  </div>
</template>

<script>
export default {
  name: "GeneralCover",
  props:{
    images:{
      type:Array,
      required:true
    },
    text:{
      type:String,
      required:true
    },
    textBold:{
      type:String,
      required:true
    },
    showButton:{
      type:Boolean,
      required:true,
    }
  },
  data(){
    return{
      img: this.images.shift()
    }
  },

  methods:{
    contactClick() {
      const element = document.getElementById("contact");
      const top = element.offsetTop;
      window.scrollTo({ left: 0, top: top, behavior: 'smooth' });
    },
  }
}
</script>

<style lang="scss">


</style>
