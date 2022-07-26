import GuideLogo from "../images/logo.png"
import { Wrapper, Content, LogoImg } from "./drawpage.styles";

const Drawpage = () => {
    const title = 'The Guiding Hand';
    const buttontext = 'Click to run the code!';
    const openInNewTab = (url) => {
        const newWindow = window.open(url, '_blank', 'noopener,noreferrer')
        if (newWindow) newWindow.opener = null
    }
    const handleClick = () => {


        openInNewTab('http://127.0.0.1:5000/my-link/')
    }
    return (
        
        <div className="draw">
                <LogoImg src={GuideLogo} alt='guide-logo' />
            <Content><h1>{title}</h1></Content>
            
            <Wrapper type="button" onClick={handleClick}>{buttontext}
            </Wrapper>
        </div>
        
    );
}

export default Drawpage;