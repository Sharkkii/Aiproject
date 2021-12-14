<template>
<div id="v-schedule-panel">
  <div class="sub-header">
    <p>Schedule Panel</p>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-schedule-panel {
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
export default {
  name: "VSchedulePanel"
}
</script>