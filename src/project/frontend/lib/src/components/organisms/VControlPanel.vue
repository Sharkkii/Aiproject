<template>
<div id="v-control-panel">
  <div class="sub-header">
    <p>Control Panel</p>
  </div>
  <v-reference-task-list v-bind:reference-task-list="referenceTaskList" v-on:create-task="createTask">
  </v-reference-task-list>
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
import VReferenceTaskList from '../molecules/VReferenceTaskList.vue'
export default {
  name: "VControlPanel",
  props: {
    referenceTaskList: {
      type: Array,
      default: []
    }
  },
  methods: {
    createTask: function(data) {
      this.$emit("create-task", data)
    }
  },
  components: {
    VReferenceTaskList
  }
}
</script>