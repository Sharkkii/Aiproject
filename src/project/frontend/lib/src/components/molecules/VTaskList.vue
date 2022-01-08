<template>
<div id="v-task-list">
  <form method="POST" v-on:submit.prevent="nop">
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
          <tr v-for="task in taskList" v-bind:key="task.id">
            <td>{{ task.name }}</td>
            <td>{{ task.required_effort }}</td>
            <td>{{ task.remaining_time }}</td>
            <td>
              <button
                type="submit"
                v-bind:name="task.name"
                v-bind:value="task.name"
                v-on:click="submit"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </form>
</div>
</template>

<style lang="scss">
#v-task-list {
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
  name: "VTaskList",
  props: {
    taskList: {
      type: Array,
      default: []
    }
  },
  methods: {
    nop: function() {},
    submit: function(event) {
      let name = event.target.name
      this.$emit("delete-task", {
        name: name
      })
    }
  }
}
</script>