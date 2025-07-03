import { Avatar, AvatarFallback, AvatarImage } from "../ui/avatar";

interface UserAvatarProps {
  userName: string;
  imageUrl?: string;
}

export function UserAvatar({ userName, imageUrl }: UserAvatarProps) {
  const initials = userName
    .split(" ")
    .map((n) => n[0])
    .join("");

  return (
    <Avatar>
      {imageUrl && <AvatarImage src={imageUrl} alt={userName} />}
      <AvatarFallback>{initials}</AvatarFallback>
    </Avatar>
  );
} 