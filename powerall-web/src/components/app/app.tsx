import * as React from 'react'
import { createMuiTheme } from '@material-ui/core'
import { ThemeProvider } from '@material-ui/core/styles'

import { loadDateSelection, storeDateSelection } from '@services'
import { Chart, Menu } from '@components'

import * as styles from './app.css'
import { DateSelection } from '@models'


const theme = createMuiTheme({
    palette: {
        primary: { main: '#8884d8' },
        secondary: { main: '#82ca9c' }
    }
})

export const App = () => {
    const [ dateSelection, setDateSelection ] = React.useState<DateSelection | null>(loadDateSelection())

    const handleDateSelection = (dateSelection: DateSelection | null) => {
        storeDateSelection(dateSelection)
        setDateSelection(dateSelection)
    }

    return (
        <ThemeProvider theme={theme}>
            <div className={styles.app}>
                <Chart dateSelection={dateSelection} />
                <Menu dateSelection={dateSelection} setDateSelection={handleDateSelection} />
            </div>
        </ThemeProvider>
    )
}