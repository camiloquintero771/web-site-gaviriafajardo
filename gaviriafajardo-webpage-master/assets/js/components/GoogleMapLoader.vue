<template>
  <div class="py-3">
    <div class="map_google" id="map"></div>
  </div>
</template>

<script>
import { Loader } from '@googlemaps/js-api-loader';

export default {
  props:{
    latitud:{
      type:Number,
      required:true
    },
    longitud:{
      type:Number,
      required:true
    }
  },

  data() {
    return {
      mapOptions: {
        center: {
          lat: this.latitud,
          lng: this.longitud
        },
        zoom: 4
      },
      loader: new Loader({apiKey: "", version: "weekly", libraries: ["places"]}),
    }
  },

  mounted() {
    this.initializeMap()
  },

  methods: {
    initializeMap() {
      this.loader
        .load()
        .then((google) => {
          new google.maps.Map(document.getElementById("map"), this.mapOptions);
        })
        .catch(e => {
          console.log(e)
        });
    }
  }
}
</script>
<style lang="scss">
.map_google{
  height: 120px;
  width: 240px;
}
</style>
