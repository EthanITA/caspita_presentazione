<template>

  <div class="card"
       style="border-color: coral;position: relative;background-color:rgba(128,128,128,0.1)">
    <div class="card-image has-text-centered">
      <figure class="inline-block">
        <img :src="require('@/assets/img/products/' + img)"/>
      </figure>
    </div>
    <div class="card-footer" style="position: absolute;bottom: 0;width: 100%">
      <div class="card-footer-item subtitle is-4">
        {{name}}
      </div>
      <div class="card-footer-item title">
        {{price}}
      </div>
      <div class="card-footer-item subtitle is-6">
        {{description}}
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Product',
    props: {
      name: {
        type: String,
        required: true
      },
      description: {
        type: String,
        default: ''
      },
      img: {
        type: String,
        required: true
      },
      price: {
        type: Number,
        required: true
      },
      old_price: {
        type: Number,
        default: 0
      },
      is_highlight: {
        type: Boolean,
        default: false
      }
    }
  };

</script>

<style scoped>
  .subtitle:not(:last-child){
    margin-bottom: 0;
  }
  img {
    max-width: 100%;
    height: 33vh;
    width: auto;
}
</style>
