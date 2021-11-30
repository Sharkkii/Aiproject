<template>
<div id="v-control-panel">
  <div class="sub-header">
    <p>Control Panel</p>
  </div>
  <v-task-create-button class="task-create-button"></v-task-create-button>
</div>
</template>

<style scoped lang="scss">
#v-control-panel {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  padding: 20px;
  width: 400px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}
</style>

<script>
import VTaskCreateButton from "../molecules/VTaskCreateButton.vue"
export default {
  name: "VControlPanel",
  components: {
    VTaskCreateButton
  }
}
</script>