<template>
  <b-carousel id="slide" :has-drag="true" :pause-hover="true" :pause-info="false" :arrow="false"
              :arrow-hover="false" style="width: 100%">

    <b-carousel-item v-for="page in pages" :key="page" class="columns has-text-centered">
      <div class="column is-one-third" v-for="row in page">

        <Product v-for="product in row" :name="product.name" :description="product.description"
                 :img="product.path" :price="product.price"
                 style="height:33vh; margin-bottom:4vh" :key="product.name + product.price"/>
      </div>
    </b-carousel-item>
  </b-carousel>
</template>

<script>
import Product from './Product.vue';

export default {
  name: 'Presentation',
  data() {
    return {
      pages: []
    }
  },
  components: {Product},
  props: {
    Product,
  },
  mounted() {
    axios.get("https://jsonblob.com/api/marcodong/caspita_srl/lucca/2c5152d6-9588-11eb-a275-d1a4d4e431b5").then((response) => {
      this.pages = response.data;
    })

  }
};
</script>

<style scoped>
</style>
