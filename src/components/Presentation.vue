<template>
  <b-carousel id="slide" :pause-info="false" :arrow="false" :v-model="page"
              :arrow-hover="false" @change="reset_loading()" :interval="interval*1000"
              style="width: 100%">

    <b-carousel-item v-for="page in pages" :key="random()" class="columns has-text-centered">
      <div class="column is-one-third" v-for="row in page">

        <Product v-for="product in row" :key="random()" :name="product.name"
                 :description="product.description"
                 :img="product.path" :price="product.price"
                 style="height:33vh; margin-bottom:4vh"/>
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
    interval: {
      type: Number,
      default: 7
    }
  },
  methods: {
    random() {
      const api = "https://random.justyy.workers.dev/api/random/?cached&n=128"
      axios.get(api).then(response => {
        return response.data
      }).catch(reason => {
        console.log(reason)
        return new Date().getTime()
      })
    },
    reset_loading(){
      this.$root.$emit('Footer')
    }
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
