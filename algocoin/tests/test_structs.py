from datetime import datetime


class TestStructs:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_MarketData(self):
        from ..lib.structs import MarketData
        from ..lib.enums import TickType, Side
        m = MarketData(time=datetime.now(),
                       volume=1.0,
                       price=1.0,
                       type=TickType.TRADE,
                       side=Side.BUY)
        # TODO no fields yet
        assert m

    def test_TradeRequest(self):
        from ..lib.structs import TradeRequest
        from ..lib.enums import Side
        t = TradeRequest(side=Side.BUY,
                         volume=1.0,
                         price=1.0)
        assert t
        # side = Side
        # volume = float
        # price = float
        # exchange = ExchangeType
        # currency = CurrencyType
        # order_type = OrderType
        # order_sub_type = OrderSubType

    def test_TradeResponse(self):
        from ..lib.structs import TradeRequest, TradeResponse, TradeResult
        from ..lib.enums import Side
        req = TradeRequest(side=Side.BUY,
                           volume=1.0,
                           price=1.0)
        t = TradeResponse(request=req,
                          side=Side.BUY,
                          volume=0.0,
                          price=0.0,
                          status=TradeResult.FILLED)
        assert t
        # side = Side
        # volume = float
        # price = float
        # success = bool
