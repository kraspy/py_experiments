from time import monotonic

from textual import on
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header, Select

select_options = [
    ('Red', 'red'),
    ('Green', 'green'),
    ('Blue', 'blue'),
]


class TimeDigits(Digits):
    """Таймер"""

    started_at = reactive(monotonic)
    current_time = reactive(0.0)
    total_time = reactive(0.0)

    def update_time(self):
        self.current_time = self.total_time + (monotonic() - self.started_at)

    def on_mount(self):
        self.timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def watch_current_time(self, current_time: float) -> None:
        minutes, seconds = divmod(current_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f'{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}')

    def start(self) -> None:
        self.started_at = monotonic()
        self.timer.resume()

    def stop(self) -> None:
        self.timer.pause()
        self.total_time += monotonic() - self.started_at
        self.current_time = self.total_time

    def reset(self) -> None:
        self.total_time = 0
        self.current_time = 0


class StopWatch(HorizontalGroup):
    """Секундомер с Buttons и TimeDisplay"""

    def compose(self):
        yield Button('Start', id='start', variant='success')
        yield Button('Stop', id='stop', variant='warning')
        yield TimeDigits('00:00:00')
        yield Button('Reset', id='reset', variant='default')
        yield Button('Remove', id='remove', variant='error')

    @on(Button.Pressed)
    def change_status(self, event: Button.Pressed):
        btn_id = event.button.id

        timer: TimeDigits = self.query_one(TimeDigits)

        if btn_id == 'start':
            timer.start()
            self.add_class('started')
        if btn_id == 'stop':
            timer.stop()
            self.remove_class('started')
        if btn_id == 'reset':
            timer.reset()
        if btn_id == 'remove':
            self.remove()


class StopWatchApp(App):
    TITLE = 'StopWatch'
    SUB_TITLE = 'Watch your life!'

    CSS_PATH = 'style.tcss'

    BINDINGS = [
        ('t', 'toggle_theme', 'Black/White Theme'),
        ('q', 'quit', 'Exit'),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield HorizontalGroup(
            Select(select_options, allow_blank=False),
            Button('Add StopWatch', id='add_stopwatch'),
        )
        yield VerticalScroll(
            StopWatch(),
            id='stopwatches',
        )
        yield Footer()

    def action_toggle_theme(self) -> None:
        self.theme = (
            'textual-dark' if self.theme == 'textual-light' else 'textual-light'
        )

    @on(Button.Pressed)
    def add_stopwatch(self, event: Button.Pressed):
        if event.button.id == 'add_stopwatch':
            stopwatch = StopWatch()
            stopwatch_container = self.query_one('#stopwatches')
            stopwatch_container.mount(stopwatch)

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.styles.background = event.value


app = StopWatchApp()
app.run()
