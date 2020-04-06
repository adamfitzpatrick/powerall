import * as React from 'react'
import { load } from '@services'
import { Chart } from '@components'
import { Ina260Measurement } from '@models'
import { DataSelection } from '../data-selection/data-selection'

export const App = () => {
    return (
        <div>
            <DataSelection />
            <Chart />
        </div>
    )
}