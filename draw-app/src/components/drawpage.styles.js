import styled from 'styled-components';

export const Wrapper = styled.button`
    display: block;
    background: #1ABC9C;
    width: 25%;
    min-width: 200px;
    height: 60px;
    border-radius: 12px;
    color: var(--white);
    border: 0;
    font-size: var(--fontBig);
    margin: 110px auto;
    transition: all 0.3s;
    outline: none;
    cursor: pointer;
    

    :hover{
        opacity: 0.8;
    }
`;

export const Content = styled.div`
    
    color:var(--medGray);
    margin-top:25px;
    border-radius:20px;
    padding: 5px;
    text-align: center;
    font-size: var(--fontSuperBig);
    


    h3{
        margin: 10px 0 0 0;
    }

    p{
        margin: 5px 0;
    }
        

    @media screen and (max-width:768px){
        display: block;
        max-height: none;
    }
`;
export const LogoImg = styled.img`
    width: 125px;
    display:flex;
    
    
   
    @media screen and (max-width: 500px){
        width: 100px;
    }
`;