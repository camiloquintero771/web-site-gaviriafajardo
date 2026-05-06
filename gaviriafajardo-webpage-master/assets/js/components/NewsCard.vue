<template>
  <div class="news-card my-3">
    <div class="card" style="width: 20rem;">
      <img :src="image" class="card-img-top news-card__image mx-auto mt-2">
      <div class="card-body">
        <p class="small mb-0">{{ textSmall }}</p>
        <h5 class="card-text fw-bold">{{ textBold }}</h5>
        <p class="small mb-0">{{ getTruncatedDescription }}</p>
        <a type="button" class="btn btn_basic-small fw-bold px-3 mt-2" :href="href">Ver</a>
      </div>
    </div>
    <div class="line mt-4"></div>
  </div>
</template>

<script>
export default {
  name: "NewsCard",
  props:{
    image:{
      type:String,
      required:true
    },
    textSmall:{
      type:String,
      required:true
    },
    textBold:{
      type:String,
      required:true
    },
    description:{
      type:String,
      required:true
    },
    href:{
      type:String,
      required:true
    }

  },
  computed: {
    getTruncatedDescription() {
      const maxLength = 40;
      const description = this.description;
      if (description.length > maxLength) {
          return description.substring(0, maxLength);
      }
      return description;
    }
  }
}
</script>

<style lang="scss">
.news-card{
  .card{
    height: 23rem;
    box-shadow: 0px 0px 15px #00000029;
    border-radius: 20px;

    .btn_basic-small{
      position: relative;
      bottom: 0px;
    }
  }

  &__image{
    width: 19rem;
    height: 12rem;
    object-fit: cover;
    object-position: center;
    border-radius: 20px;
  }

  .line{
    width: 20rem;
    background: #C20E1A;
    height: 3px;
    border-radius: 20px;
  }
}
</style>
