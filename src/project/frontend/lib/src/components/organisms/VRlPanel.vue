<template>
<div id="v-rl-panel">
  <div class="sub-header">
    <p>RL Panel</p>
  </div>
  <v-model-load-button v-on:load-model="loadModel">
  </v-model-load-button>
</div>
</template>

<style scoped lang="scss">
#v-rl-panel {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  min-height: 400px;
  padding: 20px;
  width: 600px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}
</style>

<script>
import VModelLoadButton from '../molecules/VModelLoadButton.vue'
export default {
  name: "VRlPanel",
  components: {
    VModelLoadButton
  },
  methods: {
    loadModel: function(data) {
      this.$emit("load-model", data);
    }
  }
}
</script>