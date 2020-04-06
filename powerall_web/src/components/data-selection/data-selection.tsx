import * as React from 'react'

const style: React.CSSProperties = {
    display: 'block'
}

export function DataSelection () {
    const [open, setOpen] = React.useState<boolean>(false)

    const onClick = () => setOpen(!open)
    if (!open) {
        return <button style={style} onClick={onClick}>
            <span className='material-icons settings' />
        </button>
    }
    return null
}