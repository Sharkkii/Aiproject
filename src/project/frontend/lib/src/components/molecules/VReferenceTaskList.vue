<template>
<div id="v-reference-task-list">
  <table>
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Required Effort</th>
          <th>Remaining Time</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="referenceTask in referenceTaskList" v-bind:key="referenceTask.id">
          <td>{{ referenceTask.name }}</td>
          <td>{{ referenceTask.required_effort }}</td>
          <td>{{ referenceTask.remaining_time }}</td>
          <td>
            <button>Create</button>
          </td>
        </tr>
      </tbody>
    </table>
</div>
</template>

<style lang="scss">
#v-reference-task-list {
  th, td {
    font-size: 20px;
    height: 40px;
    text-align: center;
    width: 200px;
  }
}
</style>

<script>
export default {
  name: "VReferenceTaskList",
  props: {
    referenceTaskList: {
      type: Array,
      default: []
    }
  }
}
</script>