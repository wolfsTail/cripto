import React from 'react';
import { Card } from 'antd';


function CardCryptoInstance() {

    return (
      <>
       <Card
      title={
        <div className="flex items-center gap-5">
            <img src="https://s2.coinmarketcap.com/static/img/coins/64x64/2.png"/>
            <span>LiteCoin</span>
        </div>
      }
      extra={<a href="#">More</a>}
      style={{
        width: 300,
      }}
    >
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
      </>
    )
  }
  
  export default CardCryptoInstance
  