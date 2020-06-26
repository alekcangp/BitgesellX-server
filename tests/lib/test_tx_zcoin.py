import bitgesellx.lib.tx as tx_lib

tests = [
    "0100000001000000000000000000000000000000000000000000000000000000000000"
    "000001000000fd2805c4267ec1112af809d3f18d118ae574af82a24a3311454d88aa15"
    "a2d4d51985a2d00000ee1a674c9a7abb62fce054d62c56fdf511eebb3c86301651f8d9"
    "f24b6dbc72c00000ac34e72f3af4ebb6ea84a1baf7b088f0d262934e8fa6abb974b1d3"
    "4e38dd88600100f251cbdac8a3ae679a014a5692267ed68acde7c238379788cdd9c2e4"
    "d06b1e09000015de8545abd016297392901e805bc303d9dff92e6414707c039a3bba26"
    "ac424f19aa67359d4970398d7ec9c0ec88cb7c8935176795103f07cb60e93e7d499406"
    "c8ba92b067b83bf7a42235337492f60bad0f4d3524619b436521213fd7859149ac1788"
    "6154bd82e5bcf76b1a2f54360758a834f17ebcd580548364db3ce3cdfd9ff688535b8f"
    "eb76a51744248e3fdead193a69912db593f5c7acd72a3fe17b8664dfd33a1884ae80b6"
    "18770a93c4e650dba3e0e7b082d28e162a9aa71301df35200366ae420db5d1ba79db51"
    "937aa44be1209ccb28c43ac26cf84cd9312d70f3a6a61b4ebfccebc3796090d755df74"
    "6838a923a7e408bdeca7fb961361aceceb2018f882edd38fe9fc083c03369afc218dbf"
    "9d48f64a5eaf1615b59cf71c7c79b8ac06f323782fcdef5b510e89b8cd02c9207c3cff"
    "6cc547767c67cd0dbecf479abb027de64ac57e8b368594791dbb6021edc5bc00b00d3a"
    "05789b3b2e3ab7c05170efe7d55c502327c37fad9875ca59d6249edc4d70a11c4df782"
    "c6b97bd79f80fe43c4b645a0b891b078318094d3c88db56a636502255fffa6eabb29e5"
    "18e2b33ddc49b963702f1787b6c4667630aed09a490688dc689a588471d398d3c90be9"
    "11076225935f6473737d7dfbe63b714d3a27cf07120e5c4f95d564b25830e7a7dd0261"
    "09743e2a9d078313fbe76e799fbc599e1052afc672a5573be8808254acd4a0f78fb5d9"
    "79e28bf1303ed28e88d84965925560c336202f8571d46b6a49e17a04697a15e2f195f9"
    "ec0680e5fef25b9f7003f66644da1a81257377c68a15de0f58b89927240e358388269e"
    "22855d1a605bb12d74dc954e27a31b8c5290e7ee3596a146254c4b0baaacc7c73a9f18"
    "6d580dbb951481bcba737566f7dc5ccb0ba5cfced401877db3aa7139e68411ef40cfd3"
    "a1b9a951998b20f3a3d8aef73d073ccfeeadeab56925055daed9ae93a5b1ab887f1ea1"
    "75076a9153b31fb7e581f7b0776c69583967fae7c0bd95e4d6c69a7649e6cddb3eae94"
    "1e843774aee8b5f707957cb7d12705746208431da75c5aa05be1321298b6311c22d193"
    "7afae2bdd65400008752b06f1ecc26dc59b579f9e8f20ee52d526627ecd7f4c579b2eb"
    "cf7c5aa5390000af608e02424ceeaf68cef06f6247011188724ec554e8e9163e9512c9"
    "e18978af0000117e5cf334ff7dd4858397b15235895bd76ceb9397a2d226272a5e84e5"
    "2d954d01006480c480ce0805f7377736eaebdb698f0fcd729726406691a09194de98c6"
    "09d601004d93ab877bdc866b6944dc654138b784b0dd81fd037811afff20fb85b69b61"
    "910100af16962e0f953579c123b31e211d53258d19147d5d7736656ffa23bf8a6c9b1c"
    "010018da2ac49971b595959c760e264ec6f2362d68093c5e6785da88f1204b24b02a99"
    "841a25d89984202a97c10ae2b7e9780970c6a7862991d5f97f7a21b839c6471e000000"
    "00e1f5050000000039c71b4fbdbf35e4aeabd312f560f07ff271b983d788bec185a86b"
    "03ffe691ee2103686b4bfb98e20953850634420bc147eeca3377fb726e1069a53e3fc8"
    "65744b3e40c0348010fa0c172c89eb3c87e9515516ccdc3939ef0c2a056faaf637fd9b"
    "af51001f5caaa1a654e3af936ac213fc9688b093d950865026534a2d5d09834a4408ff"
    "ffffff01605af405000000001976a914a201533465a5d9a18b958cc1eed30bc3b087e3"
    "5b88acb2e20000"
]

def test_tx_serialiazation():
    for test in tests:
        test = bytes.fromhex(test)
        deser_xzc = tx_lib.DeserializerZcoin(test)
        tx = deser_xzc.read_tx()
        assert tx.inputs[0].prev_hash == tx_lib.ZERO
        assert tx.inputs[0].prev_idx  == tx_lib.MINUS_1

