import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import LineGraph from './components/LineGraph.jsx'

export default class App extends Component {	
	render() {
    if (data) {
      console.log(data[0]['x'].length)
      return (
        <div>
          <h1>NBAStats</h1>
          <LineGraph data= { data }/>
        </div>
      )
    } else {
      return null
    }

	}
}

ReactDOM.render(<App />, document.getElementById('root'))