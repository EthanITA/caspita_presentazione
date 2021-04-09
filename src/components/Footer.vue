<template>
  <div>
    <div v-if="presentation_interval!==0" style="padding: 0.1rem 1.5rem">
      <div class="w3-light-grey w3-round-xlarge">
        <div class="w3-container w3-blue w3-round-xlarge" :style="'width:' + percent + '%'">
          <div class="subtitle has-text-light	" style="min-width: 5vw">
            {{ time_remaining.toFixed(1) }}s
          </div>
        </div>
      </div>
    </div>
    <div class="subtitle is-5 has-text-centered" style="padding:0.75rem">
      CASPITA SRL - Via Nuova per Pisa, 354, 55100 Lucca LU
    </div>
  </div>
</template>

<script>
export default {
  name: 'PresentationCompany',
  data() {
    return {
      time_remaining: this.presentation_interval,
      percent: 100,
      interval_percent_ms: 10
    }
  },
  props: {
    presentation_interval: {
      type: Number,
      default: 0
    }
  },
  methods: {
    loading: function () {
      if (this.time_remaining > 0) {
        this.time_remaining -= this.interval_percent_ms / 1000
        this.percent = this.time_remaining / this.presentation_interval * 100
      } else {
        this.presentation_next_page()
        this.reset_loading_bar()
      }
    },
    presentation_next_page() {
      this.$root.$emit('next_page')
    },
    reset_loading_bar(){
      this.time_remaining=this.presentation_interval
    }
  },
  mounted() {
    setInterval(this.loading, this.interval_percent_ms)
    this.$root.$on('reset_loading', () => {
      // your code goes here
      this.reset_loading_bar()
    })
  }
};
</script>

<style scoped>

</style>
