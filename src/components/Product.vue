<template>

  <div class="card"
       style="border-color: coral;background-color:rgba(255,255,255,0.5);">
    <div class="card-header">
      <div class="subtitle is-capitalized is-5"
           style="position:absolute;z-index: 100;">

        <div class="is-family-code	subtitle is-bold is-2 box is-underlined price-box">
          <span style="border-bottom:4px solid black;padding-bottom:2px;border-radius: 2px">
          {{ price }}€
          </span>
        </div>

      </div>
    </div>
    <div class="card-content">
      <div class="card-image" style="margin-top: -24px">
        <img :alt="name" :src="require('@/assets/img/products/' + img)"/>
      </div>
    </div>
    <div class="card-footer product-name-box">
      <div class="card-footer-item subtitle is-family-sans-serif is-capitalized is-4 product-name">
        {{ name }}
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
      type: String,
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
.subtitle:not(:last-child) {
  margin-bottom: 0;
}

.product-name-box {
  position: absolute;
  bottom: 0;
  width: 100%;
  background-color: rgba(255, 234, 184, 0.6)
}

.product-name {
  padding: 0 0 0.5rem 1rem;
  font-weight: bold;
}

img {
  max-width: 100%;
  height: 33vh;
  width: auto;
}

.price-box {
  background-color: rgba(255, 115, 0, 0.7);
  padding-top: 0;
  margin-left: 5px;
  margin-top: 5px;
  -webkit-transform: rotate(5deg);
}

</style>
