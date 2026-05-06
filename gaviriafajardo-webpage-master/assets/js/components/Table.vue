<template>
  <div class="table-vue px-6">
    <vue-good-table
      :columns="columns"
      :rows="rows"
      compactMode
      row-style-class="row-table"
      :pagination-options="{
        enabled: true,
        mode: 'pages',
        perPage: 10,
        perPageDropdown: [5, 10, 30, 50],
        dropdownAllowAll: false,
        setCurrentPage: 1,
        nextLabel: 'sig',
        prevLabel: 'ant',
        rowsPerPageLabel: 'Filas por pagína',
        ofLabel: 'de',
        pageLabel: 'pagína', // for 'pages' mode
        allLabel: 'Todo',
      }"
      :sort-options="{
        enabled: false
      }"
      :search-options="{
        enabled: true,
        placeholder: 'Buscar en tabla',
      }"
    >
      <template #emptystate>
        <h6 class="mx-auto text-center">No se encontraron coincidencias</h6>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import { VueGoodTable } from 'vue-good-table-next';


export default {
  name: "Table",
  components: { VueGoodTable, },

  props:{
    data:{
      type:Array,
      required:true
    },
  },

  data() {
    return {
      columns: [
        {
          label: 'Imagen',
          field: 'img',
          html:true,
          width:'125px',
          tdClass: 'column_img'
        },
        {
          label: 'Título',
          field: 'title',
          tdClass: 'column_title my-auto'
        },
        {
          label: 'Tipo',
          field: 'type',
          width:'125px',
          html:true,
          tdClass: 'column_title mx-auto '
        },
      ],


      rows:[]

    }
  },

  mounted(){
    this.renderRows(this.data)
  },

  methods:{
    renderRows(rows){
      var count=0
      for (const  row of rows) {
        count=count+1;
        var type=''
        if(row.type=="Servicio"){
          type='<span class="badge rounded-pill bg-danger">'+row.type+'</span>'
        }else{
          type='<span class="badge rounded-pill bg-dark">'+row.type+'</span>'
        }
        this.rows.push({id:count,img:`<a href="${row.url}"><img class="image" src="${row.img}"></a>`, title:row.title, type:type})
      }
    },
  }
}
</script>

<style lang="scss">
  .column_img{
    display: flex;
    justify-content: center;
    align-items: center;
    .image{
      width: 100px;
      height: 100px;
      object-fit: cover;
      object-position: center;
    }
  }

  .column_title{
    font-family: 'Caviar Dreams', arial;
    font-size: 20px;
  }
</style>
