<template>
<div id="v-view-monitor">
  <div class="sub-header">
    <p>View Monitor</p>
  </div>
</div>
</template>

<style scoped lang="scss">
.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}

#v-view-monitor {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  min-height: 400px;
  padding: 20px;
  width: 800px;
}
</style>

<script>
export default {
  name: "VViewMonitor"
}
</script>