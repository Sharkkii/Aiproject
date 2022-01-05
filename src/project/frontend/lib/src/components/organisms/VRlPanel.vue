<template>
<div id="v-rl-panel">
  <div class="sub-header">
    <p>RL Panel</p>
  </div>
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
export default {
  name: "VRlPanel"
}
</script>