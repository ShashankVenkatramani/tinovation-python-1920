# Storage Formats

## Users

ID of global entities are randomized based on UUID 3 (epoch mixed mode)

Global struct:
```
{
	users: Map<Int32, User>,
	schools: Map<Int32, School>,
	channels: Map<Int32, Channel>,
}
```

## School

```
{
	schoolId: Int32,

	// User ID of the members
	members: [Int32],
	// Channel ID of the owned channels
	ownedChannels: [Int32],
}
```

## Channels

Channel is the representation of a group of messages, sent by a list of users. Each user in channel can modify properties of the channel,
such as adding other users, sending messages. But only the sender himself may edit or delete a message.
Direct messages between two users are also represented as channels.

Each channel is owned by either a school or globaly (technical uses, such as direct messages).

Storage: 1 table per channel
Channel:
```
{
	channelId: Int32,

	// Messages are indexed by their ID
	messages: [Message],
	// List of channel members, stores user ID
	users: [Int32],	
}
```

Message: 
```
{
	messageId: Int32,
	
	message: String,
	reacts: [(UnicodeChar, Int32)]
	// User ID of the sender
	userId: Int32,
	// Unix epoch time
	date: Int64,
}
```
Each message has a message ID, which is used as the index in channel storage.

