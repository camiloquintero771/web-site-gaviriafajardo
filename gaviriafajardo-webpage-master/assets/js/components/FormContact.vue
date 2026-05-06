<template>
<div class="contact row " id="contact">
  <div class="col-12 col-md-7 col-lg-8 contact__text d-flex align-items-center py-5 py-md-0">
    <div class="text-start px-0 px-sm-5 px-md-1 px-lg-5">
      <span class="text-primary display-1 fw-bold title ps-1">{{ title }}</span>
      <h5 class="text-black description mt-4" v-html="description"></h5>
    </div>
  </div>
  <div class="col-12 col-md-5 col-lg-4  contact__form py-4">
    <div class="px-5 text-start">
      <form class="" :action="action" :method="method">
        <label for="fullname" class="form-label text-white fw-bold">Nombres y Apellidos</label>
        <input type="text" class="form-control bg-white opacity-50 rounded-0" id="fullname" name="name">

        <label for="email" class="form-label text-white fw-bold mt-3">Correo Electrónico</label>
        <input type="email" class="form-control bg-white opacity-50 rounded-0" id="email" name="email">

        <label for="phone" class="form-label text-white fw-bold mt-3">Celular</label>
        <input type="text" class="form-control bg-white opacity-50 rounded-0" id="phone" name="phone_number">

        <label for="asunto" class="form-label text-white fw-bold mt-3">Asunto</label>
        <textarea type="text" class="form-control bg-white opacity-50 rounded-0" id="asunto" name="subject"></textarea>

        <div class="d-flex justify-content-center mt-4 mt-sm-4">
          <button type="submit" class="btn btn_secondary fw-bold px-5 px-sm-4">Enviar</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "FormContact",

  props:{
    title:{
      type:String,
      required:true
    },
    description:{
      type:String,
      required:true
    },
    action:{
      type:String,
      required:true
    },
    method:{
      type:String,
      required:true
    },
  }
}
</script>
