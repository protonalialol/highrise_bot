from highrise import User


class PokeCommandHandler():
    async def poke_handler(self, user: User, message: str):
        self.helpers.log_debug(message=f'poke_handler called with {message} by user {user.username} [{user.id}]')
        poke_command = message.replace("!poke", "").strip(' ')

        self.helpers.log_debug(message=f'poke_command: "{poke_command}" by user {user.username} [{user.id}]')

        match poke_command:
            case "shop":
                self.helpers.log_info(message=f'"!poke shop" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "inventory":
                self.helpers.log_info(message=f'"!poke inventory" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "help":
                self.helpers.log_info(message=f'"!poke help" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_help(user=user)
            case _:
                self.helpers.log_info(message=f'default command (help) initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_help(user=user)

        return
