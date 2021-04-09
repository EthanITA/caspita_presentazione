<template>
  <b-carousel id="slide" :pause-info="false" :arrow="false" v-model="index_page"
              :arrow-hover="false" :autoplay="false" @change="reset_loading()"
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
      index_page: 0,
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
      return Math.random().toString(36).substring(7);
    },
    next_page() {
      this.index_page = (this.index_page + 1) % this.pages.length
      console.log(this.index_page)
    },
    reset_loading(){
      this.$root.$emit('reset_loading')
    }
  },
  mounted() {
    axios.get("https://jsonblob.com/api/marcodong/caspita_srl/lucca/2c5152d6-9588-11eb-a275-d1a4d4e431b5").then((response) => {
      this.pages = response.data;
    }).catch((reason => {
      console.error(reason)
    }))
    this.$root.$on('next_page', () => {
      // your code goes here
      this.next_page()
    })

  }
};
</script>

<style scoped>
</style>
